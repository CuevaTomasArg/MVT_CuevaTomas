from django.shortcuts import render
from .models import Familiar
# Create your views here.

def mostrar_familiar(request):
    F1 = Familiar(nombre="Tomas",apellido="cueva",edad=19,hijos=0,nietos=0,fecha_de_nacimiento="2022-12-07")
    F2 = Familiar(nombre="Santiago",apellido="cueva",edad=16,hijos=2,nietos=1,fecha_de_nacimiento="2006-12-24")
    F3 = Familiar(nombre="Malena",apellido="cueva",edad=19,hijos=0,nietos=0,fecha_de_nacimiento="2003-04-07")
    return render(request,'index.html',{'familia':[F1,F2,F3]})