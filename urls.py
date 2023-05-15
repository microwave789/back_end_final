from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import  voucher_form
from main import views
from .views import PostListView, PostDetailView



urlpatterns = [
    path('signup/', views.SignupPage, name='signup'),
    path('post/', views.PostListView.as_view(), name='home2'), 
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('login/', views.LoginPage, name='login'),
    path('', views.HomePage, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('menu/', views.menu, name='menu'),
    path('voucher/', voucher_form, name='voucher_form'),
    path('book_table/', views.book_table, name='book_table'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
