from django.urls import include, path
from rest_framework import routers
from proposal.views import ProposalModelViewSet

router = routers.DefaultRouter()

router.register(
    r"proposal", ProposalModelViewSet, basename="proposal"
)

urlpatterns = [
    path("", include(router.urls)),
]