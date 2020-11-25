from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
	path('new_accounts', views.user_accounts, name = 'new_accounts'),
	path('top', auth_views.LoginView.as_view(template_name = 'accounts/top.html'), name = 'top'),
	path('logout', auth_views.LogoutView.as_view(template_name = 'accounts/logout.html'), name = 'logout'),
]