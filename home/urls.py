from django.urls import path
from home import views

urlpatterns = [
    path('', views.add_form, name="add_form"),
]
