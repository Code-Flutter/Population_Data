from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_people(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    json_data = Response(serializer.data, safe=False)
    return json_data
    
@api_view(['GET'])
def get_person(request, nin):
    person = get_object_or_404(Person, nin=nin.upper())
    serializer = PersonSerializer(person)
    return Response(serializer.data)
