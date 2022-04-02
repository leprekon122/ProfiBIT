from django.shortcuts import render
from rest_framework import generics
from .models import *
import random
import time
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page

# Create your views here.

class MainPage(generics.GenericAPIView):

    @staticmethod
    def get(request):
        return render(request, 'main/main_page.html')

    def post(self, request):
        if request.POST.get('generate'):
            category = int(request.POST.get('category'))
            product = int(request.POST.get('product'))

            """create category"""
            for el in range(category):
                category_list = ['chemical', 'electronic', 'closes', 'food', 'books', 'beauty', 'build_stuff']
                Category.objects.create(name=random.choice(category_list))
            status_list = ['in_stock', 'out_of_stock']

            """create commodity"""
            for i in range(category):
                res = Category.objects.all()[i]
                for els in range(product):
                    Product.objects.create(product_name='product_number' + f"{random.randint(1, 1500)}",
                                           category=res)
        """Edit price, status, remains"""
        if request.POST.get('edit') == 'edit':
            prices = int(request.POST.get('price'))
            remains = int(request.POST.get('remains'))
            status_list = ['in_stock', 'out_of_stock']
            model = Product.objects.all()
            for el in model:
                el.price = random.randint(0, prices)
                el.status = random.choice(status_list)
                el.remains = random.randint(0, remains)
                el.save()
        return render(request, 'main/main_page.html')


"""view for ()view data page"""


class ViewData(generics.GenericAPIView):
    @staticmethod
    @cache_page(60)
    def get(request):
        model = Product.objects.all()
        paginate = Paginator(model, 50)
        page_number = request.GET.get('pages')
        page_obj = paginate.get_page(page_number)
        data = {'model': model,
                'page_obj': page_obj}
        time.sleep(2)
        return render(request, 'main/view_data.html', data)
