from django.contrib import admin
from django.urls import path
from censo import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio, name='inicio'),
    path('ingresar/', views.iniciar_sesion, name='ingresar'),
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('habitantes/', views.HabitantesListView.as_view(), name='habitantes'),
    path('habitantes/crear', views.crear_habitantes.as_view(), name='crear_habitantes'),
    path('jefes/crear', views.JefeFamiliarCrear.as_view(), name='crear_jefe'),
    path('cargas/crear', views.CargaFamiliarCrear.as_view(), name='crear_carga'),
    path('cargas/', views.CargaFamiliarList.as_view(), name='carga_familiar'),
    path('jefes/', views.JefeFamiliarList.as_view(), name='jefes_familia'),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(), name='cerrar_sesion'),
    path('habitantes/editar/<int:pk>/', views.editar_habitantes.as_view(), name='editar_habitante'),
    path('jefes/editar/<int:jefe_id>/', views.JefeFamiliarEditar.as_view(), name='editar_jefe'),
    path('cargas/editar/<int:carga_id>', views.CargaFamiliarEditar.as_view(), name='editar_carga'),
    path('jefes/eliminar/<int:pk>/', views.EliminarJefeFamiliar.as_view(), name='eliminar_jefe'),
    path('habitantes/eliminar/<int:pk>/', views.EliminarHabitante.as_view(), name='eliminar_habitante'),
    path('cargas/eliminar/<int:pk>/', views.EliminarCargaFamiliar.as_view(), name='eliminar_carga' ),
    path('habitantes/niños/', views.MostrarNiños.as_view(), name='mostrar_niños'),
    path('habitantes/ancianos/', views.MostrarAncianos.as_view(), name='mostrar_ancianos'),
    path('habitantes/discapacitados', views.MostrarDiscapacitados.as_view(), name='mostrar_discapacitados'),
    path('habitantes/hombres', views.MostrarHombres.as_view(), name='mostrar_hombres'),
    path('habitantes/mujeres', views.MostrarMujeres.as_view(), name='mostrar_mujeres'),


    
]
