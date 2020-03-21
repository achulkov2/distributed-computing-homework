from backend.models import Item
from backend.serializers import ItemSerializer

from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class ItemByIdView(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ItemsView(mixins.CreateModelMixin,
                generics.ListAPIView):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ItemPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class ItemsListView(generics.ListAPIView):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer
    pagination_class = ItemPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
