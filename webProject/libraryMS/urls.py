from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('signUp/', views.AdminSignUpView, name= 'signUp'),
    path('s_signUp/', views.StudentSignUpView, name= 's_signUp'),
    path('login/', views.loginView, name= 'login'),
    path('logout/', views.logoutView, name= 'logout'),
    path('adminProfile/', views.availableBooksView, name= 'adminProfile'),
    path('userProfile/<str:id>', views.userBorrow, name= 'userProfile'),
    path('userProfile/', views.userProfileView, name= 'userProfile'),
    path('delete/<str:id>', views.deleteView, name= 'delete'),

    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name = "pages/password_reset.html" ),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name ="pages/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name ="pages/password_reset_done.html"), 
        name="password_reset_complete"),
    
]