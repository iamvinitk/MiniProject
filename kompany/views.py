from django.http import HttpResponse
from django.shortcuts import render

from kompany.models import Laptops
# Create your views here.


def home_page(request):
    html = ''
    laptops = Laptops.objects.all()
    cont_dict = {
        'laptops_list': laptops
    }
    # for laptop in laptops:
    #     # <a href=""></a>
    #     html += '<a href=' + laptop.slug_name + '><b>' + laptop.product_name + '</b></a><br>'
    return render(request, 'home.html', cont_dict)


def laptop_details(request, name):
    laptop_list = Laptops.objects.filter(slug_name=name)
    html = ''
    if laptop_list.count() == 0:
        html = '<b><i>No Products Found!!</i></b>'
    else:
        for laptop in laptop_list:
            # <a href=""></a>
            html += '' + laptop.product_name + '<br>' + laptop.processor + '<br>' + laptop.ram + '<br>' + \
                     laptop.hdd + '<br>' + laptop.warranty + '<br>'

    return HttpResponse(html)

