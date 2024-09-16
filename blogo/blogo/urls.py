"""
URL configuration for blogo project.


"""
from django.contrib import admin

from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls")),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'index'}, name='logout'),
    path('signup/', views.signup, name='signup')

    
]
