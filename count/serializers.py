from first.serializers import OpSerializer
from .models import Entry, count
from rest_framework import serializers


class EntrySerializer(serializers.ModelSerializer):
    id = OpSerializer()
    class Meta:
        model = Entry
        fields = '__all__'

class CountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = count
        fields = '__all__'