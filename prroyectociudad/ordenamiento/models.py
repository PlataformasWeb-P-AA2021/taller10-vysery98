from django.db import models

# Create your models here.
class Parroquia(models.Model):
    class Meta:       
        verbose_name_plural = "Parroquias"
    
    opciones_tipo_parroquia = (
            ('rural','Rural'),
            ('urbana','Urbana'),
        )

    nombre = models.CharField(max_length=100)   
    tipo_parroquia = models.CharField(max_length=50, \
            choices=opciones_tipo_parroquia) 

    def __str__(self):
        return "%s - %s" % (self.nombre, 
                self.tipo_parroquia)

class Barrio(models.Model):          
    opciones_parques = (
            (1,'1'),
            (2,'2'),
            (3,'3'),
            (4,'4'),
            (5,'5'),
            (6,'6'),
        )

    nombre = models.CharField(max_length=100) 
    viviendas = models.IntegerField("Número de viviendas")
    parques = models.IntegerField("Número de parques", choices=opciones_parques)
    edificios = models.IntegerField("Número de edificios")
    parroquia = models.ForeignKey(Parroquia, related_name='barrios', 
            on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %d - %d - %d - %s" % (self.nombre, 
                self.viviendas,
                self.parques,
                self.edificios,
                self.parroquia)