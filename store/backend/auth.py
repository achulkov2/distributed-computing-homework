import requests
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class TokenVerification(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate_credentials(self, key):
        req = requests.post('http://auth:8001/auth/validate', data={'token': key})

        if req.status_code == 200:
            return User(email="kek@gmail.com", username="kek", password="veryverykek"), None

        raise AuthenticationFailed(_('Invalid token.'))