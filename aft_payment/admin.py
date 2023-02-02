# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import (
    B2CEntries,
    B2CRecipient,
    Bank,
    BankTransfer,
    BTRecipient,
    BTResponseEntry,
    BusinessToBusiness,
    BusinessToCustomer,
    Card,
    CardCheckout,
    CustomerToBusiness,
    TopupStash,
    WalletTransfer,
)


@admin.register(CustomerToBusiness)
class CustomerToBusinessAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "provider_channel",
        "phone_number",
        "currency_code",
        "amount",
        "metadata",
        "status",
        "description",
        "transaction_id",
        "provider",
    )


@admin.register(B2CRecipient)
class B2CRecipientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone_number",
        "currency",
        "amount",
        "provider_channel",
        "reason",
        "metadata",
    )
    search_fields = ("name",)


@admin.register(B2CEntries)
class B2CEntriesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone_number",
        "status",
        "transaction_id",
        "provider",
        "provider_channel",
        "value",
        "transaction_fee",
        "error_message",
    )


@admin.register(BusinessToCustomer)
class BusinessToCustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "number_queued",
        "total_value",
        "error_message",
    )
    raw_id_fields = ("recipients", "entries")


@admin.register(BusinessToBusiness)
class BusinessToBusinessAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "provider",
        "transfer_type",
        "currency_code",
        "amount",
        "destination_channel",
        "destination_account",
        "metadata",
        "status",
        "transaction_id",
        "transaction_fee",
        "provider_channel",
        "error_message",
    )


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "bank_account_name",
        "bank_account_no",
        "bank_account_code",
        "bank_account_DOB",
        "currency_code",
        "amount",
        "narration",
        "metadata",
        "status",
        "description",
        "transaction_id",
    )


@admin.register(BTRecipient)
class BTRecipientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "bank_account_name",
        "bank_account_no",
        "bank_account_code",
        "bank_account_DOB",
        "currency_code",
        "amount",
        "narration",
        "metadata",
    )


@admin.register(BTResponseEntry)
class BTResponseEntryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "account_number",
        "status",
        "transaction_id",
        "transaction_fee",
        "error_message",
    )


@admin.register(BankTransfer)
class BankTransferAdmin(admin.ModelAdmin):
    list_display = ("id", "product_name", "error_message")
    raw_id_fields = ("recipients", "entries")


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "number",
        "cvv_number",
        "expiry_month",
        "expiry_year",
        "country_code",
        "auth_token",
    )


@admin.register(CardCheckout)
class CardCheckoutAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "payment_card",
        "checkout_token",
        "currency_code",
        "amount",
        "narration",
        "metadata",
        "status",
        "description",
        "transaction_id",
    )
    list_filter = ("payment_card",)


@admin.register(WalletTransfer)
class WalletTransferAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "targetProductCode",
        "currency_code",
        "amount",
        "metadata",
        "status",
        "description",
        "transaction_id",
    )


@admin.register(TopupStash)
class TopupStashAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "currency_code",
        "amount",
        "metadata",
        "status",
        "description",
        "transaction_id",
    )
