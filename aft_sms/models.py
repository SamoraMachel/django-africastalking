from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class SentSMS(models.Model):
    status_code = [
        (100, "Processed"),
        (101, "Sent"),
        (102, "Queued"),
        (401, "RiskHold"),
        (402, "InvalidSenderId"),
        (403, "InvalidPhoneNumber"),
        (404, "UnsupportedNumberType"),
        (406, "UserInBlacklist"),
        (407, "CouldNotRoute"),
        (500, "InternalServerError"),
        (501, "GatewayError"),
        (502, "RejectedByGateway"),
    ]

    recipient = models.CharField(max_length=20)
    message = models.CharField(max_length=256)
    short_code = models.CharField(max_length=10, null=True, blank=True)
    enqueue = models.BooleanField(default=True, null=True, blank=True)
    keyword = models.CharField(max_length=100, null=True, blank=True)
    linkId = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    cost = models.CharField(max_length=20, null=True, blank=True)
    request_status = models.IntegerField(choices=status_code, null=True, blank=True)
    sms_status = models.CharField(max_length=4, null=True, blank=True)

    class Meta:
        verbose_name = _("sent_sms")
        verbose_name_plural = _("sent_sms")

    def __str__(self):
        return self.recipient

    def get_absolute_url(self):
        return reverse("sent_sms_detail", kwargs={"pk": self.pk})


class RecievedSMS(models.Model):
    message_id = models.IntegerField()
    message = models.CharField(max_length=256)
    sender = models.CharField(max_length=20)
    linkId = models.CharField(max_length=200, null=True, blank=True)
    short_code = models.CharField(max_length=10, null=True, blank=True)
    date = models.DateTimeField()

    class Meta:
        verbose_name = _("recieved_sms")
        verbose_name_plural = _("recieved_sms")

    def __str__(self):
        return self.sender

    def get_absolute_url(self):
        return reverse("recievedsms_detail", kwargs={"pk": self.pk})
