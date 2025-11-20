from django.urls import path
from auth_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register_view.as_view(),name='register'),
    path('login/',views.login_view.as_view(),name='login'),
    path('',views.dashboard_view.as_view(),name='dashboard'),
    path('resetpassword/',views.password_reset.as_view(),name='passwordreset'),
    path('logout/',views.logout__view,name='logout'),

    path("passwordreset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"), 
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("passwordreset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
