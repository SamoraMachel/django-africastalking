from django.shortcuts import render
from rest_framework import viewsets

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
from aft_payment.serializers import (
    B2CEntriesSerializer,
    B2CRecipientSerializer,
    BankSerializer,
    BankTransferSerializer,
    BTRecipientSerializer,
    BTResponseEntrySerializer,
    BusinessToBusinessSerializer,
    BusinessToCustomerSerializer,
    CardCheckoutSerializer,
    CardSerializer,
    CustomerToBusinessSerializer,
    TopupStashSerializer,
    WalletTransferSerializer,
)

# Create your views here.


class CustomerToBusinessViewSet(viewsets.ModelViewSet):
    queryset = CustomerToBusiness.objects.all()
    serializer_class = CustomerToBusinessSerializer


class BusinessToCustomerViewSet(viewsets.ModelViewSet):
    queryset = BusinessToCustomer.objects.all()
    serializer_class = BusinessToCustomerSerializer


class BusinessToBusinessViewSet(viewsets.ModelViewSet):
    queryset = BusinessToBusiness.objects.all()
    serializer_class = BusinessToBusinessSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankTransferViewSet(viewsets.ModelViewSet):
    queryset = BankTransfer.objects.all()
    serializer_class = BankTransferSerializer


class CardCheckoutViewSet(viewsets.ModelViewSet):
    queryset = CardCheckout.objects.all()
    serializer_class = CardCheckoutSerializer


class WalletTransferViewSet(viewsets.ModelViewSet):
    queryset = WalletTransfer.objects.all()
    serializer_class = WalletTransferSerializer


class TopupStashViewSet(viewsets.ModelViewSet):
    queryset = TopupStash.objects.all()
    serializer_class = TopupStashSerializer
