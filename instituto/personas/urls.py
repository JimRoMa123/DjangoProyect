#from django.conf.urls import url
from pathlib import Path
from re import template
from django.urls import path, include
from  . import views    
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns=[
    
    path("index", views.index, name="index" ),
    path("sumar", views.sumar, name="sumar" ),  
    path("calcularSuma", views.calcularSuma, name="calcularSuma" ),
    path("crud", views.list_product, name="crud" ),
    path("controlador", views.controlador, name="controlador" ),
    path("home", views.persona_crud, name="persona_crud" ),
    path("personasAdd", views.personasAdd, name="personasAdd" ),
    path('personas_del/<str:pk>', views.personas_del, name='personas_del'),
    path('personas_edit/<str:pk>', views.personas_edit, name='personas_edit'),
    path("productos", views.list_product, name="productos_crud" ),
    path("productosAdd", views.productosAdd, name="productosAdd" ),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path('productos_edit/<str:pk>', views.productos_edit, name='productos_edit'),
    path('det_prod/<str:pk>' , views.det_prod , name='det_prod' ),

    path("login/", LoginView.as_view(template_name='personas/login_per.html'), name="login_per" ),
    path('registrar/' , views.registrar , name='registrar'),
    path("logout/", LogoutView.as_view(template_name='personas/logout_per.html'), name="logout_per" ),
    path("login/", LoginView.as_view(template_name='personas/login_ad.html'), name="login_ad" ),
    path('admin/' , views.admin , name='adminsite' ),
    path('editarProducto/<idProducto>', views.editarProducto , name='editarProducto'),
    path('edicionProducto/', views.edicionProducto , name='edicionProducto'),
    path('eliminarProducto/<idProducto>', views.eliminarProducto , name='eliminarProd'),
    path('agregar/<int:idProducto>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:idProducto>/', views.eliminar_producto, name="Del"),
    path('restar/<int:idProducto>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('vercarrito/' , views.vercarrito , name='vercarrito' ),
]

