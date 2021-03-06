from django.conf.urls import patterns, url
from control import views
from django.conf import settings
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
urlpatterns=patterns(' ',url(r'^$',views.inicial, name='index'),
url(r'usuario',views.nuevoUser, name='crear'),
url(r'login/',views.login, name='crear'),
url(r'cerrar/',views.cerrar, name='crear'),
url(r'crear',views.crear, name='crear'),
url(r'mostrar',views.mostrar,name='index'),
url(r'ArticuloNevo',views.crearArticulo,name='index'),
url(r'coordenadas',views.coordenadas,name='index'),
url(r'vercoor/(?P<pkt>\d+)/',views.verCoor,name='index'),
url(r'info/(?P<nombre>\d+)/',views.infoArticulo,name='index'),
url(r'agregarubi/(?P<art>\d+)/(?P<ubi>\d+)/',views.agregarUbicacion,name='index'),
url(r'amigos/',views.buscarAmigos,name='index'),
url(r'agregar/(?P<nombre>\d+)/',views.agregarAmigos,name='index'),
url(r'username/(?P<nombre>\d+)/',views.infoPersona,name='index'),
url(r'lista/',views.lista,name='index'),
url(r'listb/(?P<nombre>\w+)/',views.lista2,name='index'),
url(r'amiList/',views.amiList,name='index'),
url(r'nuevoAmis/',views.listUser,name='index'),
url(r'nuevoAmib/(?P<nombres>\w+)/',views.listUser2,name='index'),
url(r'admin/',views.nuevoUserAdmin,name='index'),
url(r'ListaBorrar/',views.ListaBorrar,name='index'),
url(r'borrar/(?P<artb>\d+)/',views.Borrar,name='index'),
url(r'borrarcon/(?P<artb>\d+)/',views.Borrarcom,name='index'),
url(r'escribirMensaje/',views.EscribirMensaje,name='index'),
url(r'bandeja/',views.Bandeja,name='index'),
url(r'nuevoMensaje/(?P<nombre>\d+)/',views.Nmensaje,name='index'),


)


