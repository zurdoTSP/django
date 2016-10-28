from django.forms import ModelForm
from control.models import Persona, Articulo, Comentario, Puntuacion, Coordenadas, Mensaje
from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
#exclude =["user", "bottle"]
class forma(ModelForm):
	class Meta:
		model = Persona
		fields = {'nombre','imagen','sexo','edad'}

class formM(ModelForm):
	class Meta:
		model = Mensaje
		fields = {'titulo','texto'}

		#fields = "__all__"  http://www.oloblogger.com/2014/05/menu-galeria-imagenes-acordeon-css.html
class forma2(ModelForm):
	class Meta:
		model = Articulo
		fields = "__all__" 
		widgets = {'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),}


class formCoordenadas(ModelForm):
	class Meta:
		model = Coordenadas
		fields = "__all__" 
class formArt(ModelForm):
	class Meta:
		model = Articulo
		fields = {'cabecera','compania','texto','imagen'}
		widgets = {'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),}
class forma3(ModelForm):
	class Meta:
		model = Articulo
		fields = {'texto'}
class formaN(ModelForm):
	class Meta:
		model = Articulo
		fields = {'cabecera','texto','imagen'}
class forma4(ModelForm):
	class Meta:
		model = Puntuacion
		fields = {'numero'}
class forma5(forms.Form):
    your_name = forms.CharField(label='nombre de tu amigo', max_length=100)


class Buscar(forms.Form):
    buscador = forms.CharField(label='Buscar:', max_length=100)
class SingUpForm(ModelForm):
        password = forms.CharField(widget=forms.PasswordInput(render_value = False), required = True) 
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name']	
		widgets = {
			'password': forms.PasswordInput(),		
		}

class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput())
class buscar(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput())
