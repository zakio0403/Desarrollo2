from django.db import models

# Create your models here.

class departamento(models.Model):
	#Creacion de la tabla de departamentos
	id =  models.AutoField(primary_key=True)
	nombre = models.CharField(max_length = 30)

class municipio(models.Model):
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

