from rest_framework.routers import DefaultRouter
from . views import TodoItemView
from django.urls import path, include


router = DefaultRouter()
router.register(r'todoitems', TodoItemView)

urlpatterns = [
    path('', include(router.urls))
]

