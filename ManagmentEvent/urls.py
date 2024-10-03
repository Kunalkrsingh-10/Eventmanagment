"""
URL configuration for ManagmentEvent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from EventSync.views import create, retrieve_emp,delete_emp,update_emp
urlpatterns = [
    path('create_emp/',create, name='create'),
    path("admin/", admin.site.urls),
    path('',retrieve_emp, name="retrieve_emp"),
    path('delete/<int:emp_id>/',delete_emp, name="delete"),
    path('update/<int:emp_id>/',update_emp, name="update"),
]
