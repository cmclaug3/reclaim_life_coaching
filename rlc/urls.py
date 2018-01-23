"""rlc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from member.views import home, member_login, member_logout, register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('coaching/', include('coaching.urls')),

    path('register/', register, name='register'),
    path('login/', member_login, name='member_login'),
    path('logout/', member_logout, name='member_logout'),

    # FUTURE
    # change/reset email/username/password

    path('', home, name='home'),
]
