from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class UserListView(ListView):
	model = User
	template_name = 'user_list.html'
	context_object_name = 'users'
	ordering = ['username']

class UserDetailView(DetailView):
	model = User
	template_name = 'user_detail.html'
	context_object_name = 'user'
	ordering = ['username']

class UserCreateView(CreateView):
	model = User
	template_name = 'user_new.html'
	fields = ['username', 'password']
	success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
	model = User
	template_name = 'user_edit.html'
	fields = ['username']
	success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
	model = User
	template_name = 'user_delete.html'
	success_url = reverse_lazy('user_list')

class CasaListView(ListView):
	model = Casa
	template_name = 'casa_list.html'
	context_object_name = 'casas'
	ordering = ['numero_de_casa']

class CasaDetailView(DetailView):
	model = Casa
	template_name = 'casa_detail.html'
	context_object_name = 'casa'
	ordering = ['numero_de_casa']

class CasaCreateView(CreateView):
	model: Casa
	template_name = 'casa_new.html'
	fields = '__all__'
	success_url = reverse_lazy('casa_list')

class CasaUpdateView(UpdateView):
	model = Casa
	template_name = 'casa_edit.html'
	fields = '__all__'
	success_url = reverse_lazy('casa_list')

class CasaDeleteView(DeleteView):
	model = Casa
	template_name = 'casa_delete.html'
	success_url = reverse_lazy('casa_list')

class MesListView(ListView):
	model = Mes
	template_name = 'mes_list.html'
	context_object_name = 'meses'
	ordering = ['mes']

class MesDetailView(DetailView):
	model = Mes
	template_name = 'mes_detail.html'
	context_object_name = 'mes'
	ordering = ['mes']

class PagoRealizadoListView(ListView):
	model = PagoRealizado
	template_name = 'pago_realizado_list.html'
	context_object_name = 'pagos'
	ordering = ['usuario']

class PagoRealizadoDetailView(DetailView):
	model = PagoRealizado
	template_name = 'pago_realizado_detail.html'
	context_object_name = 'pago'
	ordering = ['usuario']

class PagoRealizadoCreateView(CreateView):
	model = PagoRealizado
	template_name = 'pago_realizado_new.html'
	fields = '__all__'
	success_url = reverse_lazy('pago_realizado_list')

class PagoRealizadoUpdateView(UpdateView):
	model = PagoRealizado
	template_name = 'pago_realizado_edit.html'
	fields = '__all__'
	success_url = reverse_lazy('pago_realizado_list')

class PagoRealizadoDeleteView(DeleteView):
	model = PagoRealizado
	template_name = 'pago_realizado_delete.html'
	success_url = reverse_lazy('pago_realizado_list')

