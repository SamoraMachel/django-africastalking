from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class BulkRecipient(models.Model):
    request_status = [
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

    status_code = models.IntegerField(choices=request_status)
    number = models.CharField(max_length=50)
    cost = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    message_id = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Bulk Recipient")
        verbose_name_plural = _("Bulk Recipients")

    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return reverse("BulkRecipient_detail", kwargs={"pk": self.pk})


class BulkSMS(models.Model):
    recipients = models.TextField()
    message = models.CharField(max_length=256)
    short_code = models.CharField(
        max_length=50, null=True, blank=True, default="AFRICASTKNG"
    )
    enqueue = models.BooleanField(default=True, null=True, blank=True)
    keyword = models.CharField(max_length=100, null=True, blank=True)
    link_id = models.CharField(max_length=200, null=True, blank=True)

    # response
    response_message = models.CharField(max_length=200, null=True, blank=True)
    response_recipients = models.ManyToManyField(BulkRecipient)

    class Meta:
        verbose_name = _("Bulk Sms")
        verbose_name_plural = _("Bulk Sms")

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse("bulk_sms_detail", kwargs={"pk": self.pk})
