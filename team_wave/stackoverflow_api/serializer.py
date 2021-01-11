from rest_framework import serializers
from .models import Cache

class CacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cache
        depth = 2
        fields = '__all__'