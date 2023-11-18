from django.forms import *
from django import forms
from django.forms import ModelForm
from .models import *
from datetime import date
class HabitanteForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for form in self.visible_fields():
            # print(form.field.label)
            # if form.name=='mujer_embarazada':
            #     form.field.widget.attrs['class'] = 'form-control form-check-input'
            #     form.field.widget.attrs['label'] = 'custom-control-input'
            # else:
           
            
            #print(type(label))
            if form.name=='carnet_patria':
                form.field.label = 'serial de carnet patria'
            print(form.field.label)
            label=form.field.label
            form.field.widget.attrs['placeholder'] = 'Ingrese ' + label.lower()
            # form.field.widget.attrs['class'] = 'form-control'
            # form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
        self.fields['nombre'].widget.attrs['pattern'] = "[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]*"
        self.fields['nombre'].widget.attrs['title'] = 'El nombre solo puede contener letras y espacios'
        self.fields['segundoNombre'].widget.attrs['pattern'] = "[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]*"
        self.fields['segundoNombre'].widget.attrs['title'] = 'El segundo nombre solo puede contener letras y espacios'
        self.fields['apellido'].widget.attrs['pattern'] = "[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]*"
        self.fields['apellido'].widget.attrs['title'] = 'El apellido solo puede contener letras y espacios'
        self.fields['segundoApellido'].widget.attrs['pattern'] = "[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]*"
        self.fields['segundoApellido'].widget.attrs['title'] = 'El segundo apellido solo puede contener letras y espacios'
        self.fields['mujer_embarazada'].widget.attrs['id'] = 'id_mujer_embarazada'
        self.fields['mujer_lactancia'].widget.attrs['id'] = 'id_mujer_lactancia'
        self.fields['genero'].widget.attrs['id'] = 'id_genero'
        self.fields['cedula'].widget.attrs['pattern'] = '[0-9]*'
        self.fields['cedula'].widget.attrs['title'] = 'La cédula solo puede contener números'
        self.fields['carnet_patria'].widget.attrs['pattern'] = '[0-9]*'
        self.fields['carnet_patria'].widget.attrs['title'] = 'El serial del carnet de la patria solo puede contener números'
        self.fields['discapacidad'].widget.attrs['id'] = 'id_discapacidad'
        self.fields['tipo_discapacidad'].widget.attrs['id'] = 'id_tipoDiscapacidad'
        self.fields['tipo_medicamentos'].widget.attrs['id'] = 'id_medicamentos'
        self.fields['habitante_encamada'].widget.attrs['id'] = 'id_encamada'

    class Meta:
        model = Habitante
        fields = '__all__'
        #exclude = ['cedula']

        widgets = {
            'fecha_nacimiento': DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        if fecha_nacimiento and fecha_nacimiento > date.today():
            raise forms.ValidationError(('La fecha no puede ser en el futuro.'))
        return fecha_nacimiento

class JefeForm(ModelForm):
    class Meta:
        model = JefeFamiliar
        fields = '__all__'
        exclude = ['Habitante']
    
class CargaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['jefe_familiar'].widget.attrs['id'] = 'select'

    class Meta:
        model = CargaFamiliar
        fields = '__all__'
        exclude = ['Habitante']
