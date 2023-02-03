from rest_framework import viewsets
import africastalking

from rest_framework.response import Response
from rest_framework import status

from aft_sms.models import BulkRecipient, BulkSMS
from aft_sms.serializers import (
    BulkRecipientSerializer,
    BulkSMSSerializer,
)

# Create your views here.
class BulkRecipientViewSet(viewsets.ModelViewSet):
    queryset = BulkRecipient.objects.all()
    serializer_class = BulkRecipientSerializer


class BulkSMSViewSet(viewsets.ModelViewSet):
    queryset = BulkSMS.objects.all()
    serializer_class = BulkSMSSerializer
            

    def create(self, request, *args, **kwargs):
        sms = africastalking.SMS
        response = sms.send(
            request.data["message"],
            request.data['recipients'].split(','),
            request.data.get("short_code", None),
        )
        request.data['response_message'] = response['SMSMessageData']['Message']
        rcpts_list = []
        
        for recipients in response['SMSMessageData']['Recipients']:
            print(recipients)
            recipients['status_code'] = recipients.pop('statusCode')
            recipients['message_id'] = recipients.pop('messageId')
            recpt_serializer = BulkRecipientSerializer(data=recipients)
            recpt_serializer.is_valid()
            instance = recpt_serializer.save()
            rcpts_list.append(instance.id)
        
        request.data['response_recipients'] = rcpts_list        
        return super().create(request, *args, **kwargs)
    
class PremiumSMSViewSet(viewsets.ModelViewSet):
    queryset = BulkSMS.objects.all()
    serializer_class = BulkSMSSerializer
