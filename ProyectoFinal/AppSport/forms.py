from django import forms


class SocioCrearFormulario(forms.Form):
    dni = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    mail = forms.EmailField(max_length=100)


class SocioBuscarFormulario(forms.Form):
    dni = forms.CharField(max_length=100)


class ActividadCrearFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    sede = forms.CharField(max_length=100)


class ActividadBuscarFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    sede = forms.CharField(max_length=100)


class SedeCrearFormulario(forms.Form):
    sede = forms.CharField(max_length=100)


class SedeBuscarFormulario(forms.Form):
    sede = forms.CharField(max_length=100)