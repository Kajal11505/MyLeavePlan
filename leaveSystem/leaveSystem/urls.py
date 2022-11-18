"""leaveSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('application', views.application, name="application"),
    path('applicationView', views.application_view, name="applicationView"),
    path('applicationRequests', views.application_requests, name="applicationRequests"),
    path('respond/<int:id>/<int:is_approved>', views.respond_requests, name="respondRequests")
]