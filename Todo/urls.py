from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('completed/<str:id>', views.completed_task, name="completed_task"),
    path('delete/<str:id>', views.delete_task, name='delete_task'),
    path('update/<str:id>', views.update_task, name='update_task'),
]