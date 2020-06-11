from rest_framework_simplejwt.views import token_obtain_pair, token_refresh, token_verify
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.urls import path

from backend.views import *

urlpatterns = [
    path('signup', UserView.as_view(), name="create_user"),
    path('confirm', confirm, name="confirm_user"),
    path('login', permission_classes([IsAuthenticated])(token_obtain_pair), name='obtain_token'),
    path('refresh', token_refresh, name='refresh_token'),
    path('validate', token_verify, name='validate_token')
]
