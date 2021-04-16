from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def feed(request, username=None, deu = None, habitantes = None):
	current_user = request.user

	if username and username != current_user.username:
		user = User.objects.get(username=username)
		deu = user.Deudas.all()
		habitantes = user.Profile.all()
	
	else:
		user = current_user
		habitantes = Profile.objects.filter(user = request.user)
		deu=Deudas.objects.filter(nombreD = request.user)
		tasa = TasadelMes.objects.all()
		
	return render(request, 'social/feed.html', {'user':user, 'deu':deu, 'habitantes': habitantes, 'tasa': tasa })