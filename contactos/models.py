from django.db import models

# Create your models here.
class Contactos(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    secNombre = models.CharField(max_length=50, null=True, blank=True, verbose_name='Segundo Nombre')
    apellidoP = models.CharField(max_length=50,verbose_name='Apellido Paterno' )
    apellidoM = models.CharField(max_length=50,verbose_name='Apellido Materno')
    telCasa = models.CharField(max_length=20,verbose_name='Telefono de casa')
    telCel = models.CharField(max_length=20, null=True, blank=True,verbose_name='Telefono celular')
    email = models.EmailField(max_length=254,verbose_name='Correo electronico')
    twitter = models.URLField(null=True, blank=True)
    pageWeb = models.URLField(null=True, blank=True,verbose_name='Pagina web')
    created = models.DateField(auto_now_add=True) #cada que agregas
    updated = models.DateTimeField(auto_now=True) #cada que modificas

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['apellidoP'] # - descendente; sin el - sera ascendente 

    def __str__(self):
        return '%s, %s' % (self.apellidoP, self.nombre) 