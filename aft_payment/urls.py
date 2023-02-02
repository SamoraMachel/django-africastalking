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
router.register(r"customertobusinesses", CustomerToBusinessViewSet)
router.register(r"businesstocustomers", BusinessToCustomerViewSet)
router.register(r"businesstobusinesses", BusinessToBusinessViewSet)
router.register(r"banks", BankViewSet)
router.register(r"banktransfers", BankTransferViewSet)
router.register(r"cardcheckouts", CardCheckoutViewSet)
router.register(r"wallettransfers", WalletTransferViewSet)
router.register(r"topupstashes", TopupStashViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
