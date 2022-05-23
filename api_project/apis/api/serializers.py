from pyexpat import model
from rest_framework import serializers
from apis.models import api


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','description','title')
        model = api
