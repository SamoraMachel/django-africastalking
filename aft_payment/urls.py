from django.urls import include, path
from rest_framework import routers

from aft_payment.views import (
    BankTransferViewSet,
    BankViewSet,
    BusinessToBusinessViewSet,
    BusinessToCustomerViewSet,
    CardCheckoutViewSet,
    CustomerToBusinessViewSet,
    TopupStashViewSet,
    WalletTransferViewSet,
)

router = routers.DefaultRouter()
router.register(r"C2B", CustomerToBusinessViewSet)
router.register(r"B2C", BusinessToCustomerViewSet)
router.register(r"B2B", BusinessToBusinessViewSet)
router.register(r"Bank", BankViewSet)
router.register(r"BankTransfer", BankTransferViewSet)
router.register(r"CardCheckout", CardCheckoutViewSet)
router.register(r"WalletTransfer", WalletTransferViewSet)
router.register(r"TopUpStashes", TopupStashViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
