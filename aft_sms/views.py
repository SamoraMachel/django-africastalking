from rest_framework import viewsets

from aft_sms.models import RecievedSMS, SentSMS
from aft_sms.serializers import RecievedSMSSerializer, SentSMSSerializer

# Create your views here.


class SentSMSViewSet(viewsets.ModelViewSet):
    queryset = SentSMS.objects.all()
    serializer_class = SentSMSSerializer


class RecievedSMSViewSet(viewsets.ModelViewSet):
    queryset = RecievedSMS.objects.all()
    serializer_class = RecievedSMSSerializer
