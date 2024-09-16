from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:blog_id>/', views.view_blog, name='view_blog'),
    path('blog/new/', views.new_blog, name='new_blog'),
    path('blog/<int:blog_id>/edit/', views.edit_blog, name='edit_blog'),
    path('blog/<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'index'}, name='logout'),
    path('signup/', views.signup,name='signup')

]
