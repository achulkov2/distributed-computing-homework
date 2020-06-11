from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('items/<int:pk>', views.ItemByIdView.as_view(), name='item_by_id'),
    path('items/list', views.ItemsListView.as_view(), name='items_list'),
    path('items', views.ItemsView.as_view(), name='items')
]

urlpatterns = format_suffix_patterns(urlpatterns)
