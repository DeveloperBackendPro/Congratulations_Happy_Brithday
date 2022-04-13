from django.urls import path
from sender import views

urlpatterns = [
    path('sender/', views.sender, name="sender"),
    path('wish/<str:sender>/<str:receiver>/', views.email_temp, name="email_temp")
]
