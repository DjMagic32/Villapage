from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


urlpatterns = [
	path('feed/', views.feed, name='feed'),
	path('', LoginView.as_view(template_name='social/login.html'), name='login'),
	path('logout/', logout_then_login, name='logout'),

	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)