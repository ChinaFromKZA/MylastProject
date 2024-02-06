from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from goods.models import Products

from goods.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('order_by', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug)) # нету страницы

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)
    # Пагинация

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        'title': 'Home - Каталог',
        'goods': current_page,
        "slug_url": category_slug,
    }
    return render(request, 'tovar/catalog.html', context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'tovar/product.html', context=context)
