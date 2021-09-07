"""assessment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from login import views as v1
from userdata import views as v2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.signup,name='signup'),
    path('login',v1.login,name="login"),
    path('home/',v1.home,name="home"),
    #path('addans',v2.addans,name='addans'),
    path('add/<int:pk>',v2.add,name="add"),
    path('del/<int:pk>',v2.delete,name='del'),
    path('edit/<int:pk>',v2.edit,name='edit'),
    path('delqtn/<int:pk>',v2.delqtn,name='delqtn'),
    path('addquestion',v2.addquestion,name='addquestion'),
    path('profile/',v1.profile,name='profile'),
    path('likes/<int:pk>',v2.likes,name="likes"),
    path('dislikes/<int:pk>',v2.dislikes,name="dislikes"),
    path('logout',v1.logout,name='logout')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
