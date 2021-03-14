from rest_framework import serializers
from ..models import Subject

class SubjectSerializer(serializers.ModelSerializer): # los serializers se comportan igual 
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']

