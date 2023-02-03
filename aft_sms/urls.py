from django.urls import include, path
from rest_framework import routers


from aft_sms.views import (
    BulkRecipientViewSet,
    BulkSMSViewSet,
)

router = routers.DefaultRouter()
router.register(r"SendSms", BulkSMSViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
