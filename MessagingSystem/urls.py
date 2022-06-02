from django.contrib import admin
from django.urls import path
from MessagingSystem import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/', views.new_message),
    path('messages/<int:id>', views.message_detail),
    path('messages/receiver=<receiver>', views.messages_for_spesific_receiver),
    path('messages/unread_receiver=<receiver>', views.unread_messages_for_spesific_receiver)
]