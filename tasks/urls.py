from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('update/<int:id>', views.update_task, name='update_task'),
    path('delete/<int:id>', views.delete_task, name='delete_task'),
    path('complete/<int:id>', views.complete_todo, name='complete')
]