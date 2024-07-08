from django.urls import path
from faq_chatbot import views

urlpatterns = [
    path('api/', views.ChatBotView.as_view(), name='chatbot_api')
]
