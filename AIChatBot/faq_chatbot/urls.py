from django.urls import path
from faq_chatbot import views

urlpatterns = [
    path('', views.ChatBotView.as_view(), name='home')
]
