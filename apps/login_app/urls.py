from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('register', views.registration),
    path('add_new_user', views.welcome_new_user),
    path('login', views.login),
    path('logged_in', views.success),
    path('logout', views.logout)
]