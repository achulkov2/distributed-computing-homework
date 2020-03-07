from django.urls import path

from . import views

urlpatterns = [
    path('items/<int:item_id>', views.item_by_id, name='get_or_modify_item'),
    path('items/list', views.list_items, name='list_items'),
    path('items', views.items, name='create_or_list_items')
]