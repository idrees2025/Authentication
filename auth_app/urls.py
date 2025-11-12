from django.urls import path
from auth_app import views

urlpatterns = [
    path('register/',views.register_view.as_view(),name='register'),
    path('login/',views.login_view.as_view(),name='login'),
    path('',views.dashboard_view.as_view(),name='dashboard'),
    path('resetpassword/',views.password_reset.as_view(),name='passwordreset'),
    path('logout/',views.logout__view,name='logout'),
]
