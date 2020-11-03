from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from auth.viewsets import ObtainTokenViewSet, LogoutViewSet, RegisterViewSet
from event.viewsets import EventViewSet
from user.viewsets import UserViewSet
from comment.viewsets import CommentViewSet

router = SimpleRouter()

# Auth
router.register(r'logout',  LogoutViewSet,          basename='auth-logout')
router.register(r'account', RegisterViewSet,        basename='auth-login')
router.register(r'auth',    ObtainTokenViewSet,     basename='auth-token')

# user
router.register(r'user',   UserViewSet,            basename='user')

# event
router.register(r'event',       EventViewSet,               basename='event')

event_router = NestedSimpleRouter(router, r'event', lookup='event')
event_router.register(r'comment', CommentViewSet,   basename='event-comment')


urlpatterns = [
    path(r'v1/', include(router.urls + event_router.urls)),
]

