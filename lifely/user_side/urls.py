from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.profile, name='user-profile'),
    path('todos', views.todos, name='user-todos'),
    path('todo-delete/<int:pk>/',
         views.deleteTodo, name='user-todo-delete'),
    path('events', views.events, name='user-events'),
    path('event-delete/<int:pk>/',
         views.deleteEvent, name='user-event-delete'),
    path('passwords', views.passwords, name='user-passwords'),
    path('password-delete/<int:pk>/',
         views.deletePassword, name='user-password-delete'),
    path('logout', views.logoutUser, name="logout"),
    path('change-password/', views.PasswordChangeView.as_view(
        template_name='user_side/change_password.html'), name='change-password')
]
