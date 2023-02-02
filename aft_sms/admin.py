# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import RecievedSMS, SentSMS


@admin.register(SentSMS)
class SentSMSAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "recipient",
        "message",
        "short_code",
        "enqueue",
        "keyword",
        "linkId",
        "date",
        "cost",
        "request_status",
        "sms_status",
    )
    list_filter = ("enqueue", "date")


@admin.register(RecievedSMS)
class RecievedSMSAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "message_id",
        "message",
        "sender",
        "linkId",
        "short_code",
        "date",
    )
    list_filter = ("date",)
