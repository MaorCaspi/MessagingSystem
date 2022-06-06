from django.contrib import admin
from django.urls import path
from MessagingSystem import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/', views.new_message),
    path('messages/byId/', views.message_detail),
    path('messages/all/', views.messages_for_spesific_receiver),
    path('messages/unread/', views.unread_messages_for_spesific_receiver)
]