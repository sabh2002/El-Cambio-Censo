from django.db import models
from django.forms import model_to_dict
from django.db.models import UniqueConstraint, Q

""" # Create your models here.
class jefe_familiar(models.Model):
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    genero = models.CharField(
        max_length=10, choices=(
        ('Masculino','Masculino'),
        ('Femenino','Femenino'),
        )
    )
     """
DATE_INPUT_FORMATS = ('%d-%m-%Y')

class Habitante(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    segundoNombre = models.CharField(max_length=50, verbose_name='Segundo Nombre', default='', blank=True)
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    segundoApellido = models.CharField(max_length=50, verbose_name='Segundo Apellido', default='', blank=True)
    cedula = models.CharField(max_length=10,null=True, unique=True, blank=True)
    fecha_nacimiento = models.DateField()
    ocupacion = models.CharField(max_length=100, default='No tiene')
    genero = models.CharField(max_length=10, choices=(('Femenino','Femenino'),('Masculino','Masculino')))
    estado_civil = models.CharField(max_length=20, default='No tiene', choices=(
        ('Casado','Casado'),
        ('Soltero','Soltero'),
        ('Divorciado','Divorciado'),
        ('Viudo','Viudo')
    ))
    mujer_embarazada = models.CharField(max_length=2, default='No', choices=(
    ('Sí','Sí'),('No','No')
    ))
    mujer_lactancia = models.CharField(max_length=2, default='No', choices=(
    ('Sí','Sí'),('No','No')
    ))
    discapacidad = models.CharField(max_length=2, default='No', choices=(
    ('Sí','Sí'),('No','No')
    ))
    tipo_discapacidad = models.CharField(max_length=50, blank=True, null=True)
    tipo_medicamentos = models.CharField(max_length=100, blank=True, null=True)
    habitante_encamada = models.CharField(max_length=2,default='No', choices=(
    ('Sí','Sí'),('No','No')
    ))
    carnet_patria = models.CharField(max_length=20, blank=True, null=True)
        
    vota = models.CharField(max_length=2,default='No', choices=(
    ('Sí','Sí'),('No','No')
    ))
    centro_votacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['cedula'],
                condition=Q(cedula__isnull=False),
                name='unique_cedula'
            )
        ]

    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    def toJSON(self):
        #items={'id': self.id, 'Nombre': self.nombre, 'Apellido': self.apellido }
        items = model_to_dict(self, exclude='id')
        return items
class JefeFamiliar(models.Model):
    Habitante = models.OneToOneField(Habitante, on_delete=models.CASCADE)
    tipo_casa = models.CharField(
        max_length=100, verbose_name='Tipo de Vivienda',
        choices=(
            ('Casa', 'Casa'),
            ('Apartamento', 'Apartamento'),
            ('Rancho', 'Rancho'),
            ('Anexo', 'Anexo'),
            ('Otro', 'Otro'),
            # Agrega otros tipos de viviendas según tu contexto
        )
    )
    direccion = models.CharField(max_length=100,verbose_name='Direccion',null=False)
    numeroCasa = models.PositiveIntegerField(verbose_name='Numero de Casa')
    numeroCalle = models.PositiveIntegerField(verbose_name = 'Numero de calle')
    def __str__(self):
        return f'{self.Habitante.nombre} {self.Habitante.apellido} C.I: {self.Habitante.cedula}'
    
    def toJSON(self):
        #items={'id': self.id, 'Nombre': self.nombre, 'Apellido': self.apellido }
        items = model_to_dict(self, exclude='id')
        return items

class CargaFamiliar(models.Model):
    Habitante = models.OneToOneField(Habitante, on_delete=models.CASCADE)
    jefe_familiar = models.ForeignKey(JefeFamiliar, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.Habitante.nombre} {self.Habitante.apellido} - Carga de {self.jefe_familiar}'
    
    def toJSON(self):
        #items={'id': self.id, 'Nombre': self.nombre, 'Apellido': self.apellido }
        items = model_to_dict(self, exclude='id')
        return items
