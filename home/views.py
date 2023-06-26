from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Spotlight, Brand

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home/templates/home.html'
    brand = Brand.objects.all()
    data = {
        'suv': Spotlight.objects.filter(type_id = 1)[:8],
        'sedan': Spotlight.objects.filter(type_id = 2)[:8],
        'mpv': Spotlight.objects.filter(type_id = 3)[:8],
        'cuv': Spotlight.objects.filter(type_id = 4)[:8],
        'pickup': Spotlight.objects.filter(type_id = 5)[:8],
        'hatchback': Spotlight.objects.filter(type_id = 6)[:8],
        'brand_filter': brand,
    }

    def get_brand_data(self):
        return self.brand

    def get(self, request, *args, **kwargs):
        data = self.data
        return render(request, 'home.html', data)




