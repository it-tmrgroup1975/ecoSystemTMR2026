from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('add/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),  # เพิ่มบรรทัดนี้
]
