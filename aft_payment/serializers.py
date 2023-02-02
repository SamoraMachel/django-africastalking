from rest_framework import serializers

from aft_payment.models import (
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


class CustomerToBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerToBusiness
        fields = "__all__"


class B2CRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = B2CRecipient
        fields = "__all__"


class B2CEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = B2CEntries
        fields = "__all__"


class BusinessToCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessToCustomer
        fields = "__all__"


class BusinessToBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessToBusiness
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class BTRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTRecipient
        fields = "__all__"


class BTResponseEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BTResponseEntry
        fields = "__all__"


class BankTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransfer
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class CardCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardCheckout
        fields = "__all__"


class WalletTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletTransfer
        fields = "__all__"


class TopupStashSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopupStash
        fields = "__all__"
