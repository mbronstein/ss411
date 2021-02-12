from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from ss411.users.api.views import UserViewSet
from ss411.ssoffices.api.views import SsOfficeViewSet, SsStaffViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = 'api'

router.register("users", UserViewSet, "user")
router.register("ssoffices", SsOfficeViewSet, "ssoffice")
router.register("ssstaff", SsStaffViewSet, "ssstaff")
urlpatterns = router.urls


