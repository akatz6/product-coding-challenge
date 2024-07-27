from django.urls import path
from .views import FormCreateAPIView, SectionCreateAPIView, FormUpdateAPIView

urlpatterns = [
    path('create_form/', FormCreateAPIView.as_view(), name='form-create'),
    path('draft/', SectionCreateAPIView.as_view(), name='form-draft'),
    path('publish/<uuid:pk>', FormUpdateAPIView.as_view(), name='form-publish'),
]