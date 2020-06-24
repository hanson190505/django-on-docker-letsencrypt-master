from django.urls import path

from products.views import ProductsIndex, ProductsDetail, ProductsQuery

urlpatterns = [
    path('', ProductsIndex.as_view(), name='products'),
    # 这里有一个匹配顺序问题,如果url会携带整数型参数,如id,则需要把这条url放在靠前,否则会按字符串匹配
    path('<int:pk>/', ProductsDetail.as_view(), name='product-id'),
    path('<str:s>/', ProductsQuery.as_view(), name='products-query'),
]
