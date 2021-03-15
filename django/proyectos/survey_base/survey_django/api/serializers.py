from rest_framework import serializers
from surveyf.models import Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('title', 'question', 'owner', 'active')
