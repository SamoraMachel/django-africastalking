from rest_framework import serializers

from aft_sms.models import BulkRecipient, BulkSMS


class BulkRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkRecipient
        fields = "__all__"


class BulkSMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkSMS
        fields = "__all__"
