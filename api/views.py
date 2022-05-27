from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Prognosis
from .serializers import PrognosisSerializer
from prognosis_generator import get_Prognosis
from django.db import models
import datetime
# Create your views here.

@api_view(['GET'])

def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

@api_view(['GET'])

def getPrognosis(request):
    prognosiss = Prognosis.objects.all()
    serializer = PrognosisSerializer(prognosiss, many = True)
    return Response(serializer.data)

@api_view(['GET'])

def getOnePrognosis(request, pk):
    prognosis = Prognosis.objects.get(id = pk)
    
    if(prognosis.created_at != datetime.date.today()):
        prognosis = edit(pk=pk)
        prognosis.save()

    serializer = PrognosisSerializer(prognosis, many = False)
    
    return Response(serializer.data)

def edit(pk):
    prognosis = Prognosis.objects.get(pk = pk)

    prognosis.prognosis_text = get_Prognosis()
    prognosis.save()
    return prognosis  