from django.urls import path
from faq_chatbot import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
