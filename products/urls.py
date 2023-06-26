from django.urls import path

from .views import ProductListView,BrandView

urlpatterns = [
    # Các URL khác của ứng dụng con (app)
    path('',ProductListView.as_view(), name='product_list'),
    path('<str:brand_slug>', BrandView.as_view(), name='brand_product_list'),
]