"""
URL configuration for phoenix_v_0 project.

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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('', include('gen_user.urls')),
    path('edu/', include('edu.urls')),
    path('edu/<str:pk_key>/', include('edu_stracture.urls')),
    path('edu/<str:pk_key>/', include('edu_recruiter.urls')),
    path('edu/<str:pk_key>/', include('edu_members.urls')),
    path('edu/<str:pk_key>/class/', include('edu_onLine_class.urls')),
    path('blog/', include('blogs_post.urls')),
    path('', include('edu_permissions.urls')),

]