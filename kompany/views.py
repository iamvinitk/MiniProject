from django.http import HttpResponse
from django.shortcuts import render

from kompany.models import Laptops, Mobile, ProductTypes


# Create your views here.


def home_page(request):
    html = ''
    types = ProductTypes.objects.all()
    laptops = Laptops.objects.all()[:4]
    for laptop in laptops:
        laptop.slug_name = "../../static/kompany/mobiles/"+laptop.product_name+"-0.jpeg"
        if len(laptop.product_name) > 30:
            laptop.product_name = (laptop.product_name[:30] + '..')
        else:
            laptop.product_name = laptop.product_name

    mobiles = Mobile.objects.all()[:4]
    for mobile in mobiles:
        mobile.slug_name = "../../static/kompany/mobiles/" + mobile.product_name + "-0.jpeg"
        if len(mobile.product_name) > 30:
            mobile.product_name = (mobile.product_name[:30] + '..')
        else:
            mobile.product_name = mobile.product_name

    cont_dict = {
        'types': types,
        'laptops_list': laptops,
        'mobile_list': mobiles
    }
    # for laptop in laptops:
    #     # <a href=""></a>
    #     html += '<a href=' + laptop.slug_name + '><b>' + laptop.product_name + '</b></a><br>'
    return render(request, 'home_page.html', cont_dict)


def laptop_details(request, name):
    laptop_list = Laptops.objects.filter(slug_name=name)
    print(Laptops.objects.filter(slug_name=name).query)
    html = ''
    if laptop_list.count() == 0:
        html = '<b><i>No Products Found!!</i></b>'
    else:
        for laptop in laptop_list:
            # <a href=""></a>
            html += '' + laptop.product_name + '<br>' + laptop.processor + '<br>' + laptop.ram + '<br>' + \
                     laptop.hdd + '<br>' + laptop.warranty + '<br>'

    return HttpResponse(html)


def category_view(request, category):
    objects = []
    if category == 'Laptops':
        objects = Laptops.objects.all()

    elif category == 'Mobiles':
        objects = Mobile.objects.all()
    for obj in objects:
        obj.slug_name = "../../static/kompany/mobiles/" + obj.product_name + "-0.jpeg"
    cont_dict = {
        'product_list': objects,
    }
    return render(request, 'home.html', cont_dict)
