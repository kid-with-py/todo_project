from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemView(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer