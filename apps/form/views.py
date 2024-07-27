from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Form, Step, Section
import uuid
from .serializers import FormSerializer, SectionSerializer

class FormUpdateAPIView(APIView):
    def put(self, request, *args, **kwargs):
        form = Form.objects.get(pk=kwargs['pk'])
        try:
            oldForm = Form.objects.get(name=form.name, state='current')
            oldForm.state = 'past'
            oldForm.save()
        except Form.DoesNotExist:
            pass
        form.state = 'current'
        form.save()
        serializer = FormSerializer(form)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get(self, request, *args, **kwargs):
        form = Form.objects.get(pk=kwargs['pk'])
        serializer = FormSerializer(form)
        return Response(serializer.data)
    
   
    
class SectionCreateAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        form = Form.objects.get(pk=request.data['form_id'])
        section = Section()
        section.text = request.data['text']
        section.style = request.data['style']
        section.field_id = request.data['field_id']
        section.order = request.data['order']
        section.step = Step.objects.get(pk=request.data['step_id'])
        section.save()
        serializer = SectionSerializer(section)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        section = Section.objects.all()
        serializer = SectionSerializer(section, many=True)
        return Response(serializer.data)
  
    

class FormCreateAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            form = serializer.save()
            steps = []
            for i in range(form.number_of_steps):
                step = Step()
                step.description = f'description{i + 1}'
                step.form= form
                step.order = i 
                steps.append(step)
            Step.objects.bulk_create(steps)
            form.save()
            response_serializer = FormSerializer(form)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
