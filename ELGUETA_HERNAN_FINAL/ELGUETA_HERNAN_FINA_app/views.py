from ELGUETA_HERNAN_FINA_app import forms
from django.shortcuts import render
from .models import Estudiante
from .models import Institucion
from .serializers import EstudianteSerializer
from .serializers import InstitucionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def index(request):
    return render(request, 'index.html')

def RegistroInstitucion(request):
    form = forms.RegistroInstitucion(request.POST)
    if (form.is_valid()):
        form.save()
        return index(request)
    data = {'forms': form}
    return render(request, 'inscripcion.html', data)

def agregarInstitucion(request):
    form = forms.agregar_institucionForm(request.POST)
    if (form.is_valid()):
        form.save()
        return index(request)
    data = {'forms': form}
    return render(request,'agregar_institucion.html',data)



@api_view(['GET','POST','LIST', 'PUT'])
def estudiante_datos(request):
    if request.method == 'GET':
        estude = Estudiante.objects.all()
        serial = EstudianteSerializer(estude, many=True)
        return Response(serial.data)
    if request.method == 'POST':
        serial = EstudianteSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        serial = EstudianteSerializer(estude, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE','LIST'])
def list_instituciones(request):

        if request.method == 'GET':
            insti = Institucion.objects.all()
            serial = InstitucionSerializer(insti, many=True)
            return Response(serial.data)
        if request.method == 'POST':
            serial = InstitucionSerializer(data = request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status=status.HTTP_201_CREATED)
            return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            serial.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        if request.method == 'PUT':
            serial = InstitucionSerializer(insti, data=request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data)
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
