from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from backend.serializers import UserSerializer
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.backends import TokenBackendError


class UserView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@api_view()
def confirm(request):
    try:
        payload = token_backend.decode(request.query_params.get('token'))
    except TokenBackendError:
        return Response(data={"message": "Invalid token."}, status=HTTP_400_BAD_REQUEST)
    uid = payload.get('uid', None)
    if uid is None:
        return Response(data={"message": "Invalid token."}, status=HTTP_400_BAD_REQUEST)
    user = User.objects.all().get(id=uid)
    user.is_active = True
    user.save()
    return Response(status=HTTP_200_OK)

