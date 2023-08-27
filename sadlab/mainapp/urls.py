"""
URL configuration for sadlab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('homepage/',homepage_view,name='homepage'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),

    path('plagiarism/',plagiarism_view,name='plagiarism'),
    path('manualeval/',manual_evaluation_view,name='manualeval')

    # path('file-path/', file_path_view, name='file-path'),
    # path('execution/', execution_view, name='execution'),
    # path('name-format/', name_format_view, name='name-format'),
    #path('execute_function/', execute_function, name='execute_function'),

]
