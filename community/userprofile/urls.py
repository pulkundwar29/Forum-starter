from django.urls import path
from . import views

app_name="userprofile"
urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.userRegistration, name='register'),

]
