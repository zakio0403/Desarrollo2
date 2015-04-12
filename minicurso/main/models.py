from django.db import models
from django.contrib import admin
# Create your models here.
#Construido Por Mauro Castillo 
#Lo construi para realizar pruebas con los Temples
class BodyPanelAdmin(models.Model):
#Esta clase contiene la forma como sera mostrada la pantalle principal a los usuarios
	Title = models.CharField(max_length = 30)
	Body = models.TextField()
class Departamento(models.Model):
	#Creacion de la tabla de departamentos
	id =  models.AutoField(primary_key=True)
	nombre = models.CharField(max_length = 30)

class Municipio(models.Model):
	#Creacion de la tabla de municipis
	id =  models.AutoField(primary_key=True)
	nombreMunicipio = models.CharField(max_length=30)
	iddepartamento = models.IntegerField() #Creo llave foranea a departamento

class Person(models.Model):
	#indentificador primario base de datos
	id = models.AutoField(primary_key=True)
	numberdocument = models.CharField(max_length = 30)
   	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	birthdate = models.DateTimeField()
	departemento = models.IntegerField() # creo llave foranea a departamento

class MainPost(admin.ModelAdmin):
	lis_display = ('Title','Body') 

#Agrego el modelo al panel de administracion
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(BodyPanelAdmin, MainPost)
admin.site.register(Person)

