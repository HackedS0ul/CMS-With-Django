from django.urls import path

from .views import (
    ItemList,
    ProductDetailView
)
app_name = 'cms'

urlpatterns = [
    path('item-list/', ItemList.as_view(), name='item-list'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product'),
]