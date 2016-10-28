# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render
from control.models import Mensaje
from forms import forma, forma2, forma3, forma4, forma5, formArt, formCoordenadas, formM, Buscar
def inicial(request):
	from control.models import Persona,Articulo, Mensaje
	var=False
	if not request.user.is_anonymous():
		n=True
		ps=0
		usuarios = str(request.user)
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
		
		
	else:
		n=False
	if request.method=='POST':
		form = formM(request.POST, request.FILES)
		person=Persona.objects.get(pk=nombre)
		if form.is_valid():
			tit = request.POST['titulo']
			tex = request.POST['texto']
			men=Mensaje(titulo=tit,texto=tex,destinatario=person,autor=usuarios,leido=0)
			men.save()
	else:
		form = formM()
	artAdmin=Articulo.objects.filter(creador="root192837465")
	articulo=Articulo.objects.all()
	return render_to_response("control/vista.html",locals(),context_instance=RequestContext(request))

def nuevoUser(request):
	from control.models import Persona,Articulo
	articulo=Articulo.objects.all()
# if (request.user.is_superuser and request.user.is_staff):
	if request.method == 'POST':
 # Can use standard form
 # form = UserCreationForm(request.POST)
 # Or customize it
		articulo=Articulo.objects.all()
		form = UserCreationForm(request.POST)
 		if form.is_valid():
			username = request.POST['username']
			npersona=Persona(user=username, imagen="imagenes/normalito_kBPVCpC.png",nombre="usuario", admin="no",sexo="indefinido",edad=18)
			npersona.save()
 			form.save()
 			return HttpResponseRedirect("/control")
 	else:
 # form = UserCreationForm()
 		form=UserCreationForm()
 		return render_to_response('control/usuario.html', locals(), context_instance=RequestContext(request))



def nuevoUserAdmin(request):
	from control.models import Persona,Articulo
	articulo=Articulo.objects.all()
# if (request.user.is_superuser and request.user.is_staff):
	if request.method == 'POST':
 # Can use standard form
 # form = UserCreationForm(request.POST)
 # Or customize it
		articulo=Articulo.objects.all()
		form = UserCreationForm(request.POST)
 		if form.is_valid():
			username = request.POST['username']
			if username=="root192837465":
				npersona=Persona(user=username, imagen="imagenes/normalito_kBPVCpC.png",nombre="usuario", admin="si",sexo="indefinido",edad=18)
				npersona.save()
 				form.save()
 				return HttpResponseRedirect("/control")
 	else:
 # form = UserCreationForm()
 		form=UserCreationForm()
 		return render_to_response('control/usuario.html', locals(), context_instance=RequestContext(request))





def login(request):
	from control.models import Persona,Articulo
	articulo=Articulo.objects.all()
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/control')
	if request.method=='POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			clave = request.POST['password']
			user = authenticate(username=username, password=clave)
			if user is not None:
				if user.is_active:
					auth_login(request, user)
					return HttpResponseRedirect('/control')
				else:
					return HttpResponseRedirect('/control')
			else:
					return HttpResponseRedirect('/control')

	else:
		form= AuthenticationForm()
	return render_to_response('control/login.html', locals(), context_instance=RequestContext(request))

def cerrar(request):
	logout(request)
	return render_to_response('control/vista.html', context_instance=RequestContext(request))
def coordenadas(request):
	from control.models import Persona, Articulo
	articulo=Articulo.objects.all()
	#usuarios = Jugador.objects.get(name="Fran")
	usuarios = str(request.user)
	var=False
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		n=True
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	if request.method=='POST':
		#form = forma(request.POST, instance = usuarios)
		form = formCoordenadas(request.POST, request.FILES)

		if form.is_valid():
			
			form.save()
		
	else:
		form = formCoordenadas()

	return render_to_response('control/coordenadas.html', locals(), context_instance=RequestContext(request))

def crear(request):
	from control.models import Persona,Articulo
	#usuarios = Jugador.objects.get(name="Fran")
	usuarios = request.user
	articulo=Articulo.objects.all()
	var=False
	if not request.user.is_anonymous():
		n=True
		ps=0
		usuari = str(usuarios)
		ad=Persona.objects.get(user=usuari)
		if ad.admin=="si":
			var=True
		m=Mensaje.objects.filter(destinatario__user=usuari)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	if request.method=='POST':
		#form = forma(request.POST, instance = usuarios)    Clientspin.objects.update(account_state=dinero)
		form = forma(request.POST, request.FILES)

		if form.is_valid():
			
			nombr = request.POST['nombre']
			ed=request.POST['edad']
			sex=request.POST['sexo']
			im=request.FILES['imagen']
			ec=Persona.objects.get(user=usuarios)
   			ec.nombre=nombr 
			ec.edad=ed
			ec.sexo=sex
			ec.imagen=im
    			ec.save()
			
			

		return HttpResponseRedirect('/control')
	else:
		form = forma()

	return render_to_response('control/crear.html', locals(), context_instance=RequestContext(request))
# Create your views here.

def mostrar(request):
	from control.models import Persona,Articulo
	articulo=Articulo.objects.all()
	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		n=True
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	nombre=Persona.objects.get(user=usuarios)
	articulos=Articulo.objects.filter(creador=usuarios)
	return render_to_response('control/apartado41.html', locals(), context_instance=RequestContext(request))
def ListaBorrar(request):
	from control.models import Persona,Articulo
	articulo=Articulo.objects.all()
	usuarios = str(request.user)
	ad=Persona.objects.get(user=usuarios)
	if ad.admin=="si":
		var=True
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
		n=True
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	nombre=Persona.objects.get(user=usuarios)
	articulos=Articulo.objects.filter(creador=usuarios)
	return render_to_response('control/listaborrar.html', locals(), context_instance=RequestContext(request))
def Borrar(request,artb):
	from control.models import Persona,Articulo
	articulo=Articulo.objects.all()
	usuarios = str(request.user)
	ad=Persona.objects.get(user=usuarios)
	if ad.admin=="si":
		var=True
		n=True
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	nombre=Persona.objects.get(user=usuarios)
	articulos=Articulo.objects.filter(creador=usuarios)
	boorar=Articulo.objects.get(pk=artb)
	boorar.delete()
	return HttpResponseRedirect('/control/')
	return render_to_response('control/listaborrar.html', locals(), context_instance=RequestContext(request))


def Borrarcom(request,artb):
	from control.models import Persona,Articulo, Comentario
	articulo=Articulo.objects.all()
	usuarios = str(request.user)
	ad=Persona.objects.get(user=usuarios)
	if ad.admin=="si":
		var=True
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
		n=True
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	nombre=Persona.objects.get(user=usuarios)
	articulos=Articulo.objects.filter(creador=usuarios)
	boorar=Comentario.objects.get(pk=artb)
	boorar.delete()
	return HttpResponseRedirect('/control/login')
	return render_to_response('control/listaborrar.html', locals(), context_instance=RequestContext(request))



def verCoor(request,pkt):
	from control.models import Persona,Articulo, Coordenadas
	articulo=Articulo.objects.all()
	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		n=True
		nombre=Persona.objects.get(user=usuarios)
		articulos=Articulo.objects.filter(creador=usuarios)
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False

	
	coordenada=Coordenadas.objects.get(pk=pkt)
	return render_to_response('control/vercoor.html', locals(), context_instance=RequestContext(request))
def crearArticulo(request):
	from control.models import Persona, Articulo
	articulo=Articulo.objects.all()
	#usuarios = Jugador.objects.get(name="Fran")
	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		n=True
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	if request.method=='POST':
		#form = forma(request.POST, instance = usuarios)
		form = formArt(request.POST, request.FILES)

		if form.is_valid():
			
			text = request.POST['texto']
			cab= request.POST['cabecera']
			compa= request.POST['compania']
			im=request.FILES['imagen']
			print im
			artic=Articulo(texto=text, creador=usuarios, cabecera=cab, imagen=im,compania=compa)
			artic.save()
			return HttpResponseRedirect('/control/')
		
	else:
		form = formArt()

	return render_to_response('control/crear.html', locals(), context_instance=RequestContext(request))

def infoArticulo(request,nombre):
	from control.models import Persona, Articulo, Comentario, Puntuacion, Coordenadas
	articulo=Articulo.objects.all()
	usuarios = str(request.user)
	print usuarios
	var=False
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		n=True
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False

	if n==True:
		pers=Persona.objects.get(user=usuarios)
		if pers.admin=="si":
			var=True
	comentarios=Comentario.objects.filter(Articulo__pk=nombre)
	art=Articulo.objects.get(pk=nombre)
	lista=Puntuacion.objects.filter(Articulo__pk=nombre)
	suma=0
	media=0
	listCor=Coordenadas.objects.all()
	ubicaciones=Coordenadas.objects.filter(pertenece__pk=nombre)
	for line in lista:
		suma=suma+line.numero
		media=media+1
		print suma
	if media!=0:
		suma=suma/media
		print suma
	if request.method=='POST':
		#form = forma(request.POST, instance = usuarios)
		form = forma3(request.POST)
		form2=forma4(request.POST)
		if form.is_valid():
			text = str(request.POST['texto'])
			coment=Comentario(texto=text,creador=pers,Articulo=art)
			coment.save()
			return HttpResponseRedirect('/control/info/%s/' % nombre)
		if form2.is_valid():
			num=  request.POST['numero']
			z=int(num)
			if z < 11:
				pun= Puntuacion(Articulo=art, numero=num)
				pun.save()
			return HttpResponseRedirect('/control/info/%s/' % nombre)
	else:
		form = forma3()
		form2 = forma4()
	return render_to_response('control/info.html', locals(), context_instance=RequestContext(request))
def buscarAmigos(request):
	from control.models import Persona, Articulo, Comentario, Puntuacion
	articulo=Articulo.objects.all()
	if not request.user.is_anonymous():
		n=True
		ps=0
		usuarios = str(request.user)
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	if request.method=='POST':
		#form = forma(request.POST, instance = usuarios)
		form = forma5(request.POST)
		
		if form.is_valid():
			num=  request.POST['your_name']
			nombre=Persona.objects.get(user=num)
			return render_to_response('control/buscando.html', locals(), context_instance=RequestContext(request))
	else:
		form=forma5()
	return render_to_response('control/crear.html', locals(), context_instance=RequestContext(request))

def agregarAmigos(request,nombre):
	from control.models import Persona, Articulo, Comentario, Puntuacion
	articulo=Articulo.objects.all()
	if not request.user.is_anonymous():
		n=True
		ps=0
		usuarios = str(request.user)
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	propio=Persona.objects.get(user=usuarios)
	amigo=Persona.objects.get(pk=nombre)
	propio.amigos.add(amigo)
	propio.save()
	return HttpResponseRedirect('/control/')
	return render_to_response('control/vista.html', locals(), context_instance=RequestContext(request))	



def agregarUbicacion(request,ubi,art):
	from control.models import Persona, Articulo, Comentario, Puntuacion, Coordenadas
	articulo=Articulo.objects.all()
	if not request.user.is_anonymous():
		n=True
		ps=0
		usuarios = str(request.user)
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	propio=Persona.objects.get(user=usuarios)
	arti=Articulo.objects.get(pk=art)
	ubicacion=Coordenadas.objects.get(pk=ubi)
	ubicacion.pertenece.add(arti)
	ubicacion.save()
	
	return HttpResponseRedirect('/control/info/%s/' % arti.pk)
	return render_to_response('control/vista.html', locals(), context_instance=RequestContext(request))	
def infoPersona(request,nombre):
	from control.models import Persona,Articulo
	articulo=Articulo.objects.order_by()
	if not request.user.is_anonymous():
		n=True
		ps=0
		usuarios = str(request.user)
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	name=Persona.objects.get(pk=nombre)
	articulos=Articulo.objects.filter(creador=name.user)
	return render_to_response('control/apartado42.html', locals(), context_instance=RequestContext(request))
def lista(request):
	from control.models import Persona,Articulo
	articulos=Articulo.objects.order_by("-fecha")
	articulo=Articulo.objects.all()
	if request.method=='POST':
		#form = forma(request.POST, instance = usuarios)
		form = Buscar(request.POST, request.FILES)
		if form.is_valid():
			buscar=  request.POST['buscador']
			return HttpResponseRedirect('/control/listb/%s/' % buscar)	
		
	else:
		form = Buscar()
	if not request.user.is_anonymous():
		n=True
		ps=0
		usuarios = str(request.user)
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False

	return render_to_response('control/apartado43.html', locals(), context_instance=RequestContext(request))
def lista2(request,nombre):
	from control.models import Persona,Articulo
	articulo=Articulo.objects.order_by("-fecha")
	articulos=Articulo.objects.filter(cabecera=nombre)
	if not request.user.is_anonymous():
		usuarios = str(request.user)
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		n=True
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if request.method=='POST':
		#form = forma(request.POST, instance = usuarios)
		form = Buscar(request.POST, request.FILES)
		if form.is_valid():
			buscar=  request.POST['buscador']
			return HttpResponseRedirect('/control/listb/%s/' % buscar)	
		
	else:
		form = Buscar()
	return render_to_response('control/apartado43.html', locals(), context_instance=RequestContext(request))
def amiList(request):
	from control.models import Persona,Articulo
	usuarios = str(request.user)
	x=Persona.objects.get(user=usuarios)
	articulo=Articulo.objects.all()
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		n=True
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	
	return render_to_response('control/listaAmigos.html', locals(), context_instance=RequestContext(request))

def EscribirMensaje(request):
	from control.models import Persona,Articulo
	usuarios = str(request.user)
	x=Persona.objects.get(user=usuarios)
	articulo=Articulo.objects.all()
	if not request.user.is_anonymous():
		n=True
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	
	return render_to_response('control/listaAmigos2.html', locals(), context_instance=RequestContext(request))


def listUser(request):
	from control.models import Persona,Articulo
	usuarios = str(request.user)
	x=Persona.objects.get(user=usuarios)
	articulo=Articulo.objects.all()
	usuarios=list(Persona.objects.all())
	t=x.amigos
	for line in t.all():
		usuarios.remove(line)
	usuarios.remove(x)
	if not request.user.is_anonymous():
		n=True
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	if request.method=='POST':
		#form = forma(request.POST, instance = usuarios)
		form = Buscar(request.POST, request.FILES)
		if form.is_valid():
			buscar=  request.POST['buscador']
			return HttpResponseRedirect('/control/nuevoAmib/%s/' % buscar)	
		
	else:
		form = Buscar()
	return render_to_response('control/listaNamigos.html', locals(), context_instance=RequestContext(request))
def listUser2(request,nombres):
	from control.models import Persona,Articulo
	usuarios = str(request.user)
	x=Persona.objects.get(user=usuarios)
	articulo=Articulo.objects.all()
	usuarios=list(Persona.objects.filter(nombre=nombres))
	t=x.amigos
	for line in t.all():
		usuarios.remove(line)
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		n=True
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	if request.method=='POST':
		#form = forma(request.POST, instance = usuarios)
		form = Buscar(request.POST, request.FILES)
		if form.is_valid():
			buscar=  request.POST['buscador']
			return HttpResponseRedirect('/control/nuevoAmib/%s/' % buscar)	
		
	else:
		form = Buscar()
	
	return render_to_response('control/listaNamigos.html', locals(), context_instance=RequestContext(request))

def Bandeja(request):
	from control.models import Persona,Articulo,Mensaje
	usuarios = str(request.user)
	x=Persona.objects.get(user=usuarios)
	articulo=Articulo.objects.all()
	bandeja=Mensaje.objects.filter(destinatario=x)
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		n=True
		usuarios = str(request.user)
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				i.leido=1
				i.save()
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	
	return render_to_response('control/buzon.html', locals(), context_instance=RequestContext(request))

def Nmensaje(request,nombre):
	from control.models import Persona,Articulo, Mensaje
	usuarios = str(request.user)
	articulo=Articulo.objects.all()
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		if ad.admin=="si":
			var=True
		n=True
		ps=0
		m=Mensaje.objects.filter(destinatario__user=usuarios)
		for i in m:
			if i.leido == 0:
				ps=ps+1
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/control/login')
	if request.method=='POST':
		form = formM(request.POST, request.FILES)
		person=Persona.objects.get(pk=nombre)
		if form.is_valid():
			tit = request.POST['titulo']
			tex = request.POST['texto']
			men=Mensaje(titulo=tit,texto=tex,destinatario=person,autor=usuarios,leido=0)
			men.save()
			return HttpResponseRedirect('/control/bandeja')
	else:
		form = formM()

	return render_to_response('control/Enmensaje.html', locals(), context_instance=RequestContext(request))
