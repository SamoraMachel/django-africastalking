# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import BulkRecipient, BulkSMS


@admin.register(BulkRecipient)
class BulkRecipientAdmin(admin.ModelAdmin):
    list_display = (
        'status_code',
        'number',
        'cost',
        'status',
        'message_id',
    )


@admin.register(BulkSMS)
class BulkSMSAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields' :('recipients', 'message', 'short_code', 'enqueue', 'keyword', 'link_id')}),
        ('Response', {'fields': (
            'response_message',
            'response_recipients'
        )})
    )
    list_display = (
        'short_code',
        'enqueue',
        'keyword',
        'link_id',
        'message',
    )
    def formfield_for_manytomany(self, db_field, request, **kwargs) :
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    list_filter = ('enqueue',)
    # raw_id_fields = ('response_recipients',)