from django.contrib import admin
from .models import Profile, TasadelMes, Deudas


class ProfileAdmin (admin.ModelAdmin):
    model = Profile
    list_display = ('nombre', 'apellido', 'casaN')

class DeudasAdmin(admin.ModelAdmin):
    model = Deudas
    list_display = ('nombreD', "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre" ,"Noviembre", "Diciembre", "deudatotal")


# Register your models here.
admin.site.register(Profile,ProfileAdmin)
admin.site.register(TasadelMes)
admin.site.register(Deudas, DeudasAdmin)