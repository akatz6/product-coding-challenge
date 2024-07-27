from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Form, Step
import uuid
from .serializers import FormSerializer, StepSerializer

class FormDetail(APIView):
    def get(self, request, pk, *args, **kwargs):
        form = Form.objects.get(pk=pk)
        serializer = FormSerializer(form)
        return Response(serializer.data)
   
class StepList(APIView):
    def get(self, request, *args, **kwargs):
        steps = Step.objects.all()
        serializer = StepSerializer(steps, many=True)
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
    # def post(self, request, *args, **kwargs):
    #     serializer = FormSerializer(data=request.data)
    #     if serializer.is_valid():
    #         random_uuid = uuid.uuid4()
    #         form = serializer.save()
        
    #         form.save()
    #         steps = []
    #         for i in range(form.number_of_steps):
    #             step = Step()
    #             step.name = f'name{i + 1}'
    #             step.form= form
    #             step.order = i 
    #             steps.append(step)
    #         Step.objects.bulk_create(steps)

    #         # Refresh form instance to include the created steps
    #         form.refresh_from_db()
    #         response_serializer = FormSerializer(form)
    #         return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
