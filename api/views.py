from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PatientsSerializer

from base.models import Pacients

@api_view(['GET'])
def get_all_patients(request):
    patients = Pacients.objects.all()
    serializer = PatientsSerializer(patients, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_patient(request):
    serializer = PatientsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
