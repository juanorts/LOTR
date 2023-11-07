from django.db import models
 
class Pelicula(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    titulo = models.CharField(max_length=100)
    anyo = models.IntegerField()
    director = models.CharField(max_length=50)
    duracion = models.IntegerField()
    genero = models.CharField(max_length=30)
    #Portada de la pelicula
    imagen = models.ImageField(upload_to = 'img/')

class Raza(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=20)
    tamnyo = models.CharField(max_length=20)
    caracteristica = models.CharField(max_length=20)
    actitud = models.CharField(max_length=20)
    longevidad = models.CharField(max_length=20)
    #Personaje promedio de la raza
    imagen = models.ImageField(upload_to='img/')
 
class Personaje(models.Model):
    # Campo para la relación one-to-many (un empleado pertenece a un departamento)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    # Campo para la relación many-to-many (un empleado tiene varias habilidades)
    pelicula = models.ManyToManyField(Pelicula)
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    colorOjos = models.CharField(max_length=15)
    colorPelo = models.CharField(max_length=15)
    estatura = models.IntegerField()
    # Es posible indicar un valor por defecto mediante 'default'
    imagen = models.ImageField(upload_to ='img/')
    # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True. 