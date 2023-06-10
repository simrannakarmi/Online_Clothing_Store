from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = 'users'

urlpatterns = [
    path('login_user/',views.login_user, name='login_user'),
    path('signup_user/',views.signup_user, name='signup'),
    path('logout_user/',views.logout_user, name='logout_user'),

]