"""
URL configuration for basic_crud project.

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
from basicapp import function_based_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_all_emps',function_based_view.all_employee),
    path('get_emp/<int:id>',function_based_view.get_employee),
    path('create_emp',function_based_view.create_employee),
    path('update_emp/<int:id>',function_based_view.update_employee),
    path('delete_emp/<int:id>',function_based_view.delete_employee),
]
