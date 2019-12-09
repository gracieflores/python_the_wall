from django.urls import path, include
from . import views
                    
urlpatterns = [
    path('', views.index2),
    path('/post_message', views.messageToPost),
    path('/delete_message', views.deleteMessage),
    path('/post_comment', views.commentToPost),
    path('/logoff', views.logoff),
]