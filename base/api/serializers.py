#takes python object and turns into JSON object

from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        # fields = '__all__'
        fields = ['id','name','description','updated','created','status']
        # exclude = ['host','participants']
