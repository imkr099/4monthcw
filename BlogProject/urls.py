"""BlogProject URL Configuration

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
from posts.views import main, posts_view, post_detail_view, create_post_view, MainView, PostsView
from django.conf.urls.static import static
from BlogProject.settings import MEDIA_URL, MEDIA_ROOT
from users.views import login_view, logout_view, register_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('posts/', PostsView.as_view()),
    path('posts/<int:id>/', post_detail_view),
    path('posts/create/', create_post_view),

    #users
    path('users/login/', login_view),
    path('users/logout/', logout_view),
    path('users/register/', register_view)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
