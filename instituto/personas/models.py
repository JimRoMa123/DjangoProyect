from django.db import models

# Create your models here.

class Persona(models.Model):
    rut    = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    edad   = models.IntegerField(blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)  
   
    def __str__(self):
        return self.rut+", "+ self.nombre+", "+str(self.edad)+", "+str(self.activo)

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True)  
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)



def cargarFoto(instance, filename):
    return "fotos/foto_{0}_{1}".format(instance.rut, filename )

class Alumno(Persona):
    id_genero        = models.ForeignKey('personas.Genero', models.DO_NOTHING, db_column='idGenero')
    fecha_nacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)
    foto             = models.ImageField(upload_to=cargarFoto, null=True)
    
    def __str__(self):
        return self.rut+", "+ self.nombre+", "+str(self.edad)+", "\
               +str(self.id_genero)+", "+str(self.fecha_nacimiento)+", "+str(self.activo)


def cargarFotoProducto(instance, filename):
    return "fotosProductos/foto_{0}_{1}".format(instance.idProducto,filename)


class Producto(models.Model):
    idProducto = models.IntegerField( primary_key=True)
    nombreProducto = models.CharField(max_length=30, blank=True, null=True)
    stock   = models.IntegerField(blank=True, null=True)
    precio   = models.IntegerField(blank=True, null=True)
    foto = models.ImageField(upload_to=cargarFotoProducto, null=True)
    activo = models.IntegerField(blank=True, null=True)  

    def __str__(self):
        return self.idProducto+", "+self.nombreProducto+", "+str(self.stock)\
               +", "+str(self.precio)+", "+self.foto.__str__()




