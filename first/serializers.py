from count.models import count
from rest_framework import serializers

''' Taking Admin detail with Organication serializers with the help of organication_id '''
class OpSerializer(serializers.ModelSerializer):
    class Meta:
        model = count
        fields = '__all__'

