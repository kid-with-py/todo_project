from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemView(viewsets.ModelViewSet):
    '''
    A viewset for managing TodoItem objects.

    This viewset provides CRUD operations (Create, Read, Update, Delete) for TodoItem objects.
    - `list`: Retrieves a list of all TodoItem objects.
    - `create`: Creates a new TodoItem object.
    - `update`: Updates an existing TodoItem object.
    - `destroy`: Deletes a TodoItem object from the todo list.
    '''
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def list(self, request, *args, **kwargs):
        '''
        `list`: Retrieves a list of all TodoItem objects.
        '''
        try:
            queryset = self.get_queryset()
            serializer = TodoItemSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        '''
        `create`: Creates a new TodoItem object.
        '''
        try:
            serializer = TodoItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        '''
        `update`: Updates an existing TodoItem object.
        '''
        try:
            instance = self.get_object()
            serializer = TodoItemSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        '''
        `destroy`: Deletes a TodoItem object from the todo list.
        '''
        try:
            instance = self.get_object()
            instance.delete()
            return Response({'message':'Deleted the item from the todo list'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
