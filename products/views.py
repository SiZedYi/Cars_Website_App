from typing import Any
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView

from datetime import date
from babel.numbers import format_number

from .models import Product, Brand
from home.views import HomePageView

def get_price_range(value):
        if value == '1':
            min_price = 100000000
            max_price = 299999999
        elif value == '2':
            min_price = 300000000
            max_price = 999999999
        elif value == '3':
            min_price = 1000000000
            max_price = 4999999999
        else:
            min_price = 5000000000
            max_price = 30000000000

        return min_price, max_price

def get_year_range(value):
    if value == '1':
        min_year = 1900
        max_year = 2000
    elif value == '2':
        min_year = 2001
        max_year = 2010
    elif value == '3':
        min_year = 2011
        max_year = 2020
    else:
        min_year = 2021
        max_year =  date.today().year

    return min_year, max_year
# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products.html'
    paginate_by = 2

    def get_queryset(self):
        search_query = self.request.GET.get('searchProduct')
        year_filter = self.request.GET.get('year')
        price_filter = self.request.GET.get('price')
        min_range, max_range = get_price_range(price_filter)
        min_year, max_year = get_year_range(year_filter)
        print(min_range,max_range)
        if search_query:
            queryset = Product.objects.filter(name__icontains=search_query)
        else:
            queryset = Product.objects.all()

        if price_filter:
            queryset = queryset.filter(price__range = (min_range, max_range))
        if year_filter:
            queryset = queryset.filter(car_model__range = (min_year, max_year))


        print(queryset)
        return queryset



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand_filter = HomePageView()
        data = {
            "brand_filter": brand_filter.get_brand_data(),
        }
        context.update(data)
        context[self.context_object_name] = self.get_queryset()
        # print(context)
        # Add pagination into context
        paginator = Paginator(context[self.context_object_name], self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # Format price field in the product list
        for product in page_obj:
            product.price = format_number(product.price, locale='vi_VN')
        context['product_list'] = page_obj
        # show field in queryset
        # print(context['product_list'].object_list[0].__dict__)

        return context

class BrandView(ProductListView):
    context_object_name = 'product_list_by_brand'

    def get_queryset(self, **kwargs):
        brand_slug = self.kwargs['brand_slug']
        brand = get_object_or_404(Brand, name=brand_slug)
        queryset = super().get_queryset()
        queryset = queryset.filter(brand_id=brand.brand_id)
        # print(queryset)
        return queryset

