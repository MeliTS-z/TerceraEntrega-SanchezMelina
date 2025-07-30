from django.urls import path

#include
from .views import landing, crear_amigo, crear_transitador, gracias, ofrecer_donacion, grdonacion, buscar_amigos, amigo, buscar_transitadores, transitador, SOSrefugioCreateView, SOSrefugioListView, aec, SOSrefugioDetailView, SOSrefugioDeleteView, SOSrefugioUpdateView

urlpatterns = [
    path('', landing, name='landing'),
    #path('landing', landing),
    #path('crear-amigo/<str:nombre>/', crear_amigo),
    path('crear-amigo/', crear_amigo, name='crear_amigo'),
    path('crear-transitador/', crear_transitador, name='crear_transitador'),
    path('gracias/', gracias, name='gracias'),
    path('ofrecer-donacion/', ofrecer_donacion, name='ofrecer_donacion'),
    path('gracias-donacion/', grdonacion, name='grdonacion'),
    path('amigos/', amigo, name='amigo'),
    path('buscar-amigos/', buscar_amigos, name='buscar_amigos'),
    path('transitadores/', transitador, name='transitador'),
    path('buscar-transitadores/', buscar_transitadores, name='buscar_transitadores'),
    path('SOS-refugio/', SOSrefugioCreateView.as_view(), name='SOS_refugio'),
    path('lista-SOS/', SOSrefugioListView.as_view(), name='lista_SOS'),
    path('ayuda-en-camino/', aec, name='ayuda_en_camino'),
    path('detalle-listar-SOS/<int:pk>', SOSrefugioDetailView.as_view(), name='detalle_listar_SOS'),
    path('eliminar-SOS-refugio/<int:pk>', SOSrefugioDeleteView.as_view(), name='eliminar_SOS_refugio'),
    path('editar-SOS-refugio/<int:pk>', SOSrefugioUpdateView.as_view(), name='editar_SOS_refugio')


]

#path('admin/', admin.site.urls),

