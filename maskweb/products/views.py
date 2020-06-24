from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView

from products.models import Products


class ProductsIndex(ListView):
    model = Products

    def get_queryset(self):
        # print(self.kwargs['s'])
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsIndex, self).get_context_data()
        print(context)
        return context


class ProductsQuery(ListView):
    template_name = 'products/product_query.html'
    model = Products
    context_object_name = 'products_query'

    def get_queryset(self):
        print(self.kwargs['s'])
        if self.kwargs['s'] == 'mask':
            return get_list_or_404(Products, category=1)
        elif self.kwargs['s'] == 'glove':
            return get_list_or_404(Products, category=2)


class ProductsDetail(DetailView):
    queryset = Products.objects.all()
    template_name = 'products/product_detail.html'
