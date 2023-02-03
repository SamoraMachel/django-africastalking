from django.shortcuts import render
from rest_framework import viewsets

import africastalking

from aft_payment.models import (
    Bank,
    BankTransfer,
    BusinessToBusiness,
    BusinessToCustomer,
    CardCheckout,
    CustomerToBusiness,
    TopupStash,
    WalletTransfer,
)
from aft_payment.serializers import (
    BankSerializer,
    BankTransferSerializer,
    BusinessToBusinessSerializer,
    BusinessToCustomerSerializer,
    CardCheckoutSerializer,
    CustomerToBusinessSerializer,
    TopupStashSerializer,
    WalletTransferSerializer,
    CardSerializer
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
    
    def create(self, request, *args, **kwargs):
        card_checkout = africastalking.Payment
        payment_card =  request.data.get('payment_card', None),
        
        response = card_checkout.card_checkout(
            request.data['product_name'],
            request.data['currency_code'],
            request.data['amount'],
            payment_card[0],
            request.data.get('checkout_token', None),
            request.data['narration'],
            request.data.get('metadata', {})
        )
        
        request.data['status'] = response['status']
        request.data['description'] = response['description']
        request.data['transaction_id'] = response.get("transactionId", None)
        
        if (payment_card is not None) :
            card_serializer = CardSerializer(data=payment_card[0])
            card_serializer.is_valid()
            instance = card_serializer.save()
            request.data['payment_card'] = instance.id
    
        
        return super().create(request, *args, **kwargs)

class WalletTransferViewSet(viewsets.ModelViewSet):
    queryset = WalletTransfer.objects.all()
    serializer_class = WalletTransferSerializer


class TopupStashViewSet(viewsets.ModelViewSet):
    queryset = TopupStash.objects.all()
    serializer_class = TopupStashSerializer
