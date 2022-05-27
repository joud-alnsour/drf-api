from rest_framework import serializers
from apis.models import Api

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','description','purshaser','timestamp','updated')
        model = Api
