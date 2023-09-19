from rest_framework import serializers
from base.models import Pacients


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacients
        fiels = '__all__'