from ast import Try
from email import message
from logging import exception
from msilib.schema import ListView
from multiprocessing import context
from django.shortcuts import render, get_object_or_404 , redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Persona, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from personas.carrito import Carrito
# Create your views here.
'''
class Persona:
    #rut=""
    #nombre=""
    #edad=0

    def __init__(self,rut,nombre,edad):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad

    def getRut(self):
        return self.rut

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad    

    def toString(self):
        return self.rut+", "+self.nombre+", "+str(self.edad)


p1 =  Persona("1-1","Susana",22)
p2 =  Persona("2-2","Juan",19)
p3 = Persona("3-3","Sandra",20)
personas = [p1,p2,p3]
'''

def persona_crud(request):
    print("estoy en Persona Crud...")
    context={} 
    return render(request,"personas/personas_add.html",context)


def personasAdd(request):
    print("estoy en controlador PersonasAdd...")
    context={}
    if request.method == "POST":
        print("contralador es un post...") 
        opcion=request.POST.get("opcion","")
        print("opcion="+opcion)
        #Listar
        if opcion=="Editar" or opcion == "Volver":
            personas = Persona.objects.all()
            context ={'personas':personas}
            print("enviando datoa personas_edit")
            return render(request,"personas/personas_list.html",context) 
        #Agregar
        if opcion=="Agregar":
            rut=request.POST["rut"]
            nombre=request.POST["nombre"]
            edad=request.POST["edad"]
       
            if rut != "" and nombre != "" and edad !="":
                persona = Persona(rut, nombre, edad) 
                persona.save()
                context={'mensaje':"Ok, datos grabados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}

           #Agregar
        if opcion=="Actualizar":
            rut=request.POST["rut"]
            nombre=request.POST["nombre"]
            edad=request.POST["edad"]
       
            if rut != "" and nombre != "" and edad !="":
                persona = Persona(rut, nombre, edad) 
                persona.save()
                context={'persona':persona,'mensaje':"Ok, datos actualizados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}
            return render(request,"personas/personas_edit.html",context) 


    return render(request,"personas/personas_add.html",context)   


def personas_del(request, pk):
    mensajes=[]
    errores=[]
    personas = Persona.objects.all()
    try:
        persona=Persona.objects.get(rut=pk)
        context={}
        if persona:
           persona.delete()
           mensajes.append("Bien, datos eliminados...")

           context = {'personas': personas,  'mensajes': mensajes, 'errores':errores}

           return render(request, 'personas/personas_list.html', context)

    except:
        print("Error, rut no existe")
        errores.append("Error rut no encontrado.")
        context = {'personas': personas,  'mensajes': mensajes, 'errores':errores}
        return render(request, 'personal/personas_list.html', context)

def personas_edit(request, pk):
    mensajes=[]
    errores=[]
   
    
    context={}
    personas = Persona.objects.all()
    #try:
    persona=Persona.objects.get(rut=pk)

    context={}
    if persona:
        print("Edit encontró a persona...")
        mensajes.append("Bien, datos eliminados...")

        context = {'persona': persona,  'mensajes': mensajes, 'errores':errores}

        return render(request, 'personas/personas_edit.html', context)
    '''
    except:
        print("Error, rut no existe")
        errores.append("Error rut no encontrado.")
        context = {'personas': personas,  'mensajes': mensajes, 'errores':errores}
        return render(request, 'personas/personas_list.html', context)
    '''
    '''
    if jugador:
        form = FormJugador(request.POST or None,
                            request.FILES or None, instance=jugador)
        #form = FormJugador(instance=jugador)
        print("estoy en jugador true")
        if request.method == 'POST':
            print("ingresó al POST")
            #form = FormJugador(request.POST, request.FILES)
           # print("formulario id_persona: " + form.id_persona)
            if form.is_valid():
                print("is valid...")
                jugador = form.save()
                jugador.save()
                mensajes.append("Bien!, datos grabados...")
                print("Bien!, datos grabados...")
                accion = 'tabla'
                context = {'jugadores': jugadores, 'mensajes': mensajes,
                           'errores': errores, 'accion': accion}
            else:
                errores.append("Error!, datos no grabados...del EDIT")
                print("Error!, datos no grabados... form="+str(form.errors))
                accion='tabla'
                context = {'jugadores': jugadores, 'mensajes': mensajes,
                       'errores': errores, 'accion': accion}

            return render(request, 'personal/crud_jugador.html', context)
        else:
            mensajes.append("Bien!, id existe...")
            print("entró al else form=Jugador()...")
            accion = 'form_edit'
            context = {'jugadores': jugadores, 'mensajes': mensajes,
                       'errores': errores,'form':form, 'accion': accion}
    '''               
    return render(request, 'personas/personas_list.html', context)
    '''
    else:
        print("Error, id_jugador no existe")
        errores.append("Error id no encontrado.")
        accion='tabla'
        context = {'jugadores': jugadores,  'mensajes': mensajes,
                   'errores':errores,'accion':accion}
    return render(request, 'personal/crud_jugador.html', context)
    '''

def index(request):
    print("Hola estoy en index del views")

    dias =["lunes","martes","miércoles","jueves","viernes","sábado"]
  
    context={
             'nombre':'Cristián García',
             'carrera':'Analista Programador',
             'idJornada': 2,
             'dias': dias,
             
            }

    return render(request,"personas/index.html",context)

def sumar(request):
    print("estoy en sumar...")
    context={} 
    return render(request,"personas/suma.html",context)






def calcularSuma(request):
    print("estoy en calcular...")

    if request.method == "POST" :
       print("es un post...") 
       v1 = request.POST.get("valor1",'0')
       v2 = request.POST.get("valor2",'0')
       print(v1,"     ",v2)
       resultado = int(v1) + int(v2)

    context={'v1':v1, 'v2':v2,'resultado':resultado}   
    #return redirect(reverse('sumar') +"?"+str(resultado) )
    return render(request,"personas/suma.html",context)


def crud(request):
    print("estoy en crud...")
    context={}
    return render(request,"personas/crud.html",context)


def controlador(request):
    print("estoy en controlador...")
    context={}
    if request.method == "POST":
        print("contralador es un post...") 
        opcion=request.POST.get("opcion","")
        print("opcion="+opcion)
        #Listar
        if opcion=="Listar":
           context={"personas":personas}
       
        #Buscar
        if opcion=="Buscar":
            rut=request.POST.get("rut","")
            if rut != "":
                for persona in personas:
                    print("entro al for con el rut ", rut)
                    if persona.getRut() == rut:
                        print("buscar encontro el rut")
                        context={'persona':persona}
                        break
            else:
                context={'mensaje':"Error, rut no debe estar vacio"}
        #Agregar
        if opcion == "Agregar":
             rut=request.POST.get("rut","")
             nombre=request.POST.get("nombre","")
             edad=int(request.POST.get("edad","0"))
            
             if rut != "" and nombre != "" and edad!="":
                nuevo = Persona(rut, nombre, edad) 
                if personas.append(nuevo) == None:
                    context={'mensaje':"Ok agregado"}
                else:
                    context={'mensaje':"Error, datos no agregado"}
             else:
                context={'mensaje':"Error, los campos no deben estar vacios"}

           
    return render(request,"personas/crud.html",context)

##################   P R O D U C T O S ######################
 
def productos_crud(request):
    print("estoy en Productos Crud...")
    context={} 
    return render(request,"personas/productos_add.html",context)

def productosAdd(request):
    print("estoy en controlador ProductosAdd...")
    context={}
    if request.method == "POST":
        print("contralador productos es un post...") 
        opcion=request.POST.get("opcion","")
        print("opcion="+opcion)
        #Listar
        if opcion=="Editar" or opcion == "Volver":
            productos = Producto.objects.all()
            context ={'productos':productos}
            print("enviando datos a productos_list")
            return render(request,"personas/productos_list.html",context) 
        #Agregar
        if opcion=="Agregar":
            idProducto=request.POST["idProducto"]
            nombreProducto=request.POST["nombreProducto"]
            stock=int(request.POST["stock"])
            precio=int(request.POST["precio"])
            fotoProducto=request.FILES["fotoProducto"]

       
            if idProducto != "" and nombreProducto != "" and stock >=0 and precio >=0:

                producto = Producto(idProducto, nombreProducto, stock, precio,
                                    fotoProducto) 
                producto.save()
                context={'mensaje':"Ok, datos grabados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}

           #Agregar
        if opcion=="Actualizar":
            idProducto=request.POST["idProducto"]
            nombreProducto=request.POST["nombreProducto"]
            stock=int(request.POST["stock"])
            precio=int(request.POST["precio"])
            try:
                fotoProducto=request.FILES["fotoProducto"]
            except:
                fotoProducto=""
       
            if idProducto != "" and nombreProducto != "" and stock >=0 \
                and precio >=0:

                producto = Producto(idProducto, nombreProducto, stock, precio,
                                    fotoProducto) 
                producto.save()
                context={'mensaje':"Ok, datos grabados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}
            return render(request,"personas/productos_edit.html",context) 


    return render(request,"personas/productos_add.html",context)   

def productos_del(request, pk):
    mensajes=[]
    errores=[]
    productos = Producto.objects.all()
    try:
        producto=Producto.objects.get(idProducto=pk)
        context={}
        if producto:
           producto.delete()
           mensajes.append("Bien, datos eliminados...")

           context = {'productos': productos,  'mensajes': mensajes, 'errores':errores}

           return render(request, 'personas/productos_list.html', context)

    except:
        print("Error, rut no existe")
        errores.append("Error rut no encontrado.")
        context = {'productos': productos,  'mensajes': mensajes, 'errores':errores}
        return render(request, 'personal/productos_list.html', context)

def productos_edit(request, pk):
    mensajes=[]
    errores=[]   
    
    context={}
    #productos = Producto.objects.all()
    #try:
    producto=Producto.objects.get(idProducto=pk)

    context={}
    if producto:
        print("Edit encontró a producto...")
        mensajes.append("Bien, datos eliminados...")

        context = {'producto': producto,  'mensajes': mensajes, 'errores':errores}

        return render(request, 'personas/productos_edit.html', context)
    
    return render(request, 'personas/productos_list.html', context)


def list_product(request):
    productos= Producto.objects.all()
    return render(request, "personas/productos_add.html" , 
    {"productos": productos})


def det_prod(request , pk):
    
    mensajes=[]
    errores=[]
    producto = Producto.objects.all()
    producto= Producto.objects.filter(idProducto=pk)
    return render(request, "personas/det_prod.html", {"productos": producto})

def login(request):
    
    persona = Persona.objects.all()
    return render(request, "personas/login_per.html" , {"persona": persona})



def registrar(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request , f'Usuario {username} creado')
            return redirect('productos_crud')
    else:
        form = UserRegisterForm()
    
    context= {'form' : form }
    return render(request , 'personas/registrar.html' , context)



def admin(request):
    producto = Producto.objects.all()
    messages.success(request, '¡Producto listados!')
    return render(request, "personas/admin.html", {"producto": producto})

       




def editarProducto(request, idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    return render(request, "personas/editarProducto.html", {"producto": producto})


def edicionProducto(request):
    idProducto = request.POST['idProducto']
    nombre = request.POST['nombreProducto']
    stock = request.POST['stock']
    
    Precio = request.POST['precio']
    Activo = request.POST['activo']
    

    producto = Producto.objects.get(idProducto=idProducto)
    producto.nombreProducto = nombre
    producto.stock = stock
    producto.precio = Precio
    producto.activo = Activo
    
    producto.save()

    messages.success(request, '¡Producto actualizado!')

    return redirect("adminsite")


def eliminarProducto(request, idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    producto.delete()

    messages.success(request, '¡Producto eliminado!')

    return redirect("adminsite")

def agregar_producto(request, idProducto):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=idProducto)
    carrito.agregar(producto)
    return redirect("crud")

def eliminar_producto(request, idProducto):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=idProducto)
    carrito.eliminar(producto)
    return redirect("crud")

def restar_producto(request, idProducto):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=idProducto)
    carrito.restar(producto)
    return redirect("crud")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("crud")

def vercarrito(request):
    productos= Producto.objects.all()
    return render(request, "personas/carrito.html" , 
    {"productos": productos})