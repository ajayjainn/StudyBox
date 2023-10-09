from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('logout',views.logout_, name='logout'),
    path('tasks', views.tasks, name='tasks')
]