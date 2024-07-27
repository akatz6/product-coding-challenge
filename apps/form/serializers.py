from rest_framework import serializers
from.models import Form, Field, Step

        
class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
        
# class StepSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Step
#         fields = '__all__'
        
# class FormSerializer(serializers.ModelSerializer):
#     form = StepSerializer(many=True, read_only=True)
#     class Meta:
#         model = Form
#         fields = '__all__'
        
# class StepSerializer(serializers.ModelSerializer):
#     step = FormSerializer(many=True, read_only=True)
#     class Meta:
#         model = Step
#         fields = '__all__'
    
class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"

class FormSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Form
        fields = "__all__"
        

