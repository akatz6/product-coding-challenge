from django.urls import path
from .views import FormCreateAPIView, StepList, FormDetail
urlpatterns = [
    path('create_form/', FormCreateAPIView.as_view(), name='form-create'),
    path('steps/', StepList.as_view(), name='steps-list'),
    path('create/<uuid:pk>/', FormDetail.as_view(), name='reviews'),
]