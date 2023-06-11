from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# def admin_login(request):
#     try:
#         if request.user.is_authenticated:
#             return redirect('/home/')
#         if request.method == 'POST'