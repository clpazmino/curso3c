from django.shortcuts import render

# Create your views here.
def holamundoCore(request):
  return render(request,'core.html')

def inicio(request):
  return render(request,'inicio.html')

def acerca(request):
  return render(request,'acerca.html')

def portafolio(request):
  return render(request,'portafolio.html')

def contacto(request):
  return render(request,'contacto.html')
