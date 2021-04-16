from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model): #HABITANTES!!
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name = 'Profile')
    nombre = models.CharField(max_length=300, null =True)
    apellido = models.CharField(max_length=300, null =True)
    casaN = models.CharField(max_length=40, null =  True)
    
    def __str__(self):
        return f'Perfil de {self.user.username}'
    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
            .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
        
    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
            .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)


class TasadelMes(models.Model):

    Tabla = models.CharField(max_length = 10)

    Tenero = models.IntegerField( null =  True)
    DolarenEnero = models.IntegerField( null =  True)
    PagodeEnero = models.IntegerField("Enero", null= True)

    Tfebrero = models.IntegerField( null =  True)
    Dolarenfebrero = models.IntegerField( null =  True)
    PagodeFebrero = models.IntegerField("Febrero", null= True)

    Tmarzo = models.IntegerField( null =  True)
    Dolarenmarzo = models.IntegerField( null =  True)
    PagodeMarzo = models.IntegerField("Marzo", null= True)

    Tabril = models.IntegerField( null =  True)
    Dolarenabril = models.IntegerField( null =  True)
    PagodeAbril = models.IntegerField( null= True)

    Tmayo = models.IntegerField( null =  True)
    Dolarenmayo = models.IntegerField( null =  True)
    PagodeMayo = models.IntegerField( null= True)

    Tjunio = models.IntegerField( null =  True)
    Dolarenjunio = models.IntegerField( null =  True)
    PagodeJunio = models.IntegerField( null= True)

    Tjulio = models.IntegerField( null =  True)
    Dolarenjulio = models.IntegerField( null =  True)
    PagodeJulio = models.IntegerField( null= True)

    Tagosto = models.IntegerField( null =  True)
    Dolarenagosto = models.IntegerField( null =  True)
    PagodeAgosto = models.IntegerField( null= True)

    Tseptiembre = models.IntegerField( null =  True)
    Dolarenseptiembre = models.IntegerField( null =  True)
    PagodeSeptiembre = models.IntegerField( null= True)

    Toctubre = models.IntegerField( null =  True)
    Dolarenoctubre = models.IntegerField( null =  True)
    PagodeOctubre = models.IntegerField( null= True)

    Tnoviembre = models.IntegerField( null =  True)
    Dolarennoviembre = models.IntegerField( null =  True)
    PagodeNoviembre = models.IntegerField( null= True)

    Tdiciembre = models.IntegerField( null =  True)
    Dolarendicimebre = models.IntegerField( null =  True)
    PagodeDiciembre = models.IntegerField( null= True)

    PagoPromedio = models.IntegerField( null= True)

    @property
    def PagodeEnero(self):
        pago =  self.Tenero * self.DolarenEnero 

        return pago
    
    @PagodeEnero.setter
    def PagodeEnero(self, value):
        self.PagodeEnero = value

    @property
    def PagodeFebrero(self):
        pagoF =  self.Tfebrero * self.Dolarenfebrero

        return pagoF

    @PagodeFebrero.setter
    def PagodeFebrero(self, value):
        self.PagodeFebrero = value

    @property
    def PagodeMarzo(self):
        pagoM =  self.Tmarzo * self.Dolarenmarzo

        return pagoM

    @PagodeMarzo.setter
    def PagodeMarzo(self, value):
        self.PagodeMarzo = value

    @property
    def PagodeAbril(self):
        pagoA =  self.Tabril * self.Dolarenabril

        return pagoA

    @PagodeAbril.setter
    def PagodeAbril(self, value):
        self.PagodeAbril = value

    @property
    def PagodeMayo(self):
        pagoMa =  self.Tmayo * self.Dolarenmayo

        return pagoMa

    @PagodeMayo.setter
    def PagodeMayo(self, value):
        self.PagodeMAyo = value

    @property
    def PagodeJunio(self):
        pagoJ =  self.Tjunio * self.Dolarenjunio

        return pagoJ

    @PagodeJunio.setter
    def PagodeJunio(self, value):
        self.PagodeJunio = value

    @property
    def PagodeJulio(self):
        pagoJJ =  self.Tjulio * self.Dolarenjulio

        return pagoJJ

    @PagodeJulio.setter
    def PagodeJulio(self, value):
        self.PagodeJulio = value

    @property
    def PagodeAgosto(self):
        pagoAg =  self.Tagosto * self.Dolarenagosto

        return pagoAg

    @PagodeAgosto.setter
    def PagodeAgosto(self, value):
        self.PagodeAgosto = value

    @property
    def PagodeSeptiembre(self):
        pagoS =  self.Tseptiembre * self.Dolarenseptiembre

        return pagoS

    @PagodeSeptiembre.setter
    def PagodeSeptimebre(self, value):
        self.PagodeSeptiembre = value

    @property
    def PagodeOctubre(self):
        pagoO =  self.Toctubre * self.Dolarenoctubre

        return pagoO

    @PagodeOctubre.setter
    def PagodeOctubre(self, value):
        self.PagodeOctubre = value

    @property
    def PagodeNoviembre(self):
        pagoN =  self.Tnoviembre * self.Dolarennoviembre

        return pagoN

    @PagodeNoviembre.setter
    def PagodeNoviembre(self, value):
        self.PagodeNoviembre = value


    @property
    def PagodeDiciembre(self):
        pagoD =  self.Tdiciembre * self.Dolarendicimebre

        return pagoD

    @PagodeDiciembre.setter
    def PagodeDiciembre(self, value):
        self.PagodeDiciembre = value


    @property
    def PagoPromedio(self):
        pagoPromo =  ((self.PagodeDiciembre + self.PagodeNoviembre + self.PagodeOctubre 
        + self.PagodeSeptiembre + self.PagodeAgosto + self.PagodeJulio + self.PagodeJunio + self.PagodeMayo 
        + self.PagodeAbril + self.PagodeMarzo + self.PagodeFebrero + self.PagodeEnero)/12)

        return pagoPromo

    @PagoPromedio.setter
    def PagoPromedio(self, value):
        self.PagoPromedio = value
    
    def __str__(self):
        return self.Tabla


class Deudas(models.Model):
    nombreD = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'Deudas')
    Tabla_año = models.ForeignKey( TasadelMes, on_delete=models.CASCADE, null = True)

    Enero =  models.BooleanField(": Enero", default=False)
    Febrero = models.BooleanField(": Febrero", default=False)
    Marzo = models.BooleanField(": Marzo", default=False)
    Abril = models.BooleanField(": Abril", default=False)
    Mayo = models.BooleanField(": Mayo", default=False)
    Junio = models.BooleanField(": Junio", default=False)
    Julio = models.BooleanField(": Julio", default=False)
    Agosto = models.BooleanField(": Agosto", default=False)
    Septiembre = models.BooleanField(": Septiembre", default=False)
    Octubre = models.BooleanField(": Octubre", default=False)
    Noviembre = models.BooleanField(": Noviembre", default=False)
    Diciembre = models.BooleanField(": Diciembre", default=False)


    deudatotal = models.IntegerField( null = True)

    deudadepago = models.IntegerField( null = True)


    def __str__(self):
        return self.nombreD.username

    @property
    def deudatotal(self):
        t= 0
        teta = [self.Tabla_año.PagodeEnero, self.Tabla_año.PagodeFebrero, self.Tabla_año.PagodeMarzo,self.Tabla_año.PagodeAbril, self.Tabla_año.PagodeMayo, self.Tabla_año.PagodeJunio, self.Tabla_año.PagodeJulio, self.Tabla_año.PagodeAgosto, self.Tabla_año.PagodeSeptiembre, self.Tabla_año.PagodeOctubre, self.Tabla_año.PagodeNoviembre, self.Tabla_año.PagodeDiciembre]
        mes = [self.Enero,self.Febrero,self.Marzo, self.Abril ,self.Mayo, self.Junio, self.Julio, self.Agosto, self.Septiembre, self.Octubre, self.Noviembre, self.Diciembre]
        for m , y in zip(mes,teta):
            if m != True:
                t = y + t
                continue
            else:
                continue
        return t
    
    @deudatotal.setter
    def deudatotal(self, value):
        self.deudatotal = value