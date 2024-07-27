from rest_framework import serializers
from.models import Form, Field


class Form(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
        
class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
