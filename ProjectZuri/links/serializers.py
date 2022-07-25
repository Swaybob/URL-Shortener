from rest_framework import serializers
from . import models


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Links
        fields = '__all__'
