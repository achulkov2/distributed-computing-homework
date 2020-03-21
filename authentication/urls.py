from rest_framework_simplejwt.views import token_obtain_pair, token_refresh, token_verify
from django.urls import path

from authentication.views import *

urlpatterns = [
    path('signup', UserView.as_view(), name="create_user"),
    path('login', token_obtain_pair, name='obtain_token'),
    path('refresh', token_refresh, name='refresh_token'),
    path('validate', token_verify, name='validate_token')
]
