from rest_framework import serializers
from.models import Form, Field, Step, Section


        
        
class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['id', 'option']

class SectionSerializer(serializers.ModelSerializer):
    field = FieldSerializer(read_only=True)
    class Meta:
        model = Section
        fields = ['id', 'text','style', 'field', 'order' ]
        
    
class StepSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    class Meta:
        model = Step
        fields = ['id', 'description', 'order','sections'  ]

class FormSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Form
        fields = ['id', 'name', 'number_of_steps','state','steps']
        

        

