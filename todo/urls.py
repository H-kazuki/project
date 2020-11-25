from django.urls import path
from . import views


app_name = 'todo'

urlpatterns = [
		path('', views.index, name = 'index'),
		path('<int:id>/delete', views.delete, name = 'delete'),
		path('<int:id>/edit', views.edit, name = 'edit'),
		path('todo/<str:category>/', views.todo_category, name = 'todo_category'),
		path('create', views.create, name = 'create'),
]