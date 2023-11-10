from django.db import models
 
class Pelicula(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    titulo = models.CharField(max_length=100)
    anyo = models.IntegerField()
    director = models.CharField(max_length=50)
    duracion = models.IntegerField()
    genero = models.CharField(max_length=30)
    #Portada de la pelicula
    imagen = models.ImageField(upload_to = 'img/', default = 'img/default.jpg')

    def __str__(self):
        return self.titulo

class Raza(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=20, default = 'null')
    tamnyo = models.CharField(max_length=20, default = 'null')
    caracteristica = models.CharField(max_length=20, default = 'null')
    actitud = models.CharField(max_length=20, default = 'null')
    longevidad = models.CharField(max_length=20, default = 'null')
    #Personaje promedio de la raza
    imagen = models.ImageField(upload_to='img/', default = 'img/default.jpg')

    def __str__(self):
        return self.nombre
 
class Personaje(models.Model):
    # Campo para la relación one-to-many (un empleado pertenece a una raza)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    # Campo para la relación many-to-many (un personaje aparece en varias peliculas)
    pelicula = models.ManyToManyField(Pelicula)
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    colorOjos = models.CharField(max_length=15)
    colorPelo = models.CharField(max_length=15)
    estatura = models.IntegerField()
    # Es posible indicar un valor por defecto mediante 'default'
    imagen = models.ImageField(upload_to ='img/', default = 'img/default.jpg')
    # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True. 

    def __str__(self):
        return self.nombre