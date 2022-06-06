from django.contrib import admin
from django.urls import path
from MessagingSystem import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/', views.new_message),
    path('messages/get_by_id/', views.message_detail),
    path('messages/get_all/', views.messages_for_spesific_receiver),
    path('messages/get_all_unread/', views.unread_messages_for_spesific_receiver)
]