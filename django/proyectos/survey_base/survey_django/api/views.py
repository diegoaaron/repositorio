from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view # primer método
from rest_framework.views import APIView # segundo métod
from rest_framework.response import Response

from surveyf.models import Survey
from.serializers import SurveySerializer

"""
@api_view(['GET', 'POST'])
def survey_list(request):
    ''' Listar las encuestas o crear una nueva '''
    if request.method == 'GET':
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            
            return Response(serializer.erros, status=status.HTTP_400_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def survey_details(request, pk):
    ''' Obtener, actualizar o eliminar una encuesta específica '''
    try:
        survey = Survey.objects.get(pk=pk)

    except Survey.DoesNotExist:
        
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SurveySerializer(survey)

        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SurveySerializer(survey, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        survey.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
"""

class SurveyList(APIView):
    ''' Lista de todas las encuestas y crear una nueva encuesta'''
    def get(sef, request, format=None):
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SurveyDetails(APIView):
    '''obtener, actualizar, eliminar una encuesta específica'''
    def get_object(self, pk):
        try:
            return Survey.objects.get(pk=pk)

        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = SurveySerializer(survey)

        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = SurveySerializer(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)