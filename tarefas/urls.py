from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.view_lista_tarefas, name='lista'),
    path('nova/', views.view_nova_tarefa, name='nova'),
    path('editar/<int:tarefa_id>', views.view_editar_tarefa, name='editar'),
    path('apagar/<int:tarefa_id>', views.view_apagar_tarefa, name='apagar'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),
]