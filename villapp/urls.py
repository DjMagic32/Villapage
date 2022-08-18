from django.urls import path
from .views import CasaCreateView,CasaUpdateView, CasaDeleteView, CasaListView, CasaDetailView
from .views import UserCreateView, UserUpdateView, UserDeleteView, UserListView, UserDetailView
from .views import PagoRealizadoListView, PagoRealizadoDetailView, PagoRealizadoCreateView, PagoRealizadoUpdateView, PagoRealizadoDeleteView
from .views import MesListView, MesDetailView  
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


urlpatterns = [
    path('casa/new/', CasaCreateView.as_view(), name='casa_new'),
    path('casa/<int:pk>/edit/', CasaUpdateView.as_view(), name='casa_edit'),
    path('casa/<int:pk>/delete/', CasaDeleteView.as_view(), name='casa_delete'),
    path('casa/', CasaListView.as_view(), name='casa_list'),
    path('casa/<int:pk>/', CasaDetailView.as_view(), name='casa_detail'),
    path('user/new/', UserCreateView.as_view(), name='user_new'),
    path('user/<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('pago/new/', PagoRealizadoCreateView.as_view(), name='pago_new'),
    path('pago/<int:pk>/edit/', PagoRealizadoUpdateView.as_view(), name='pago_edit'),
    path('pago/<int:pk>/delete/', PagoRealizadoDeleteView.as_view(), name='pago_delete'),
    path('pago/', PagoRealizadoListView.as_view(), name='pago_list'),
    path('pago/<int:pk>/', PagoRealizadoDetailView.as_view(), name='pago_detail'),
    path('mes/new/', MesListView.as_view(), name='mes_new'),
    path('mes/<int:pk>/edit/', MesDetailView.as_view(), name='mes_edit'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)