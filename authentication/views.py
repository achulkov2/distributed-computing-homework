from rest_framework import mixins
from rest_framework import generics

from django.contrib.auth.models import User
from authentication.serializers import UserSerializer


class UserView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               generics.GenericAPIView):
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
