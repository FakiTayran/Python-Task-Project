"""AS_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from howmanytimes.views import getOperations
from howmanytimes.views import bin_create
from howmanytimes.views import getBins
from howmanytimes.views import getBin
from howmanytimes.views import bin_update
from howmanytimes.views import bin_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',getOperations),
    path('Add/',bin_create),
    path('Get/',getBins),
    path('Detail/<str:id>/', getBin),
    path('Update/<str:id>',bin_update),
    path('Delete/<str:id>',bin_delete),
    path('Update/',getBins),
    path('Delete/',getBins)
]
