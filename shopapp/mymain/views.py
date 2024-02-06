from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Домой',
        'content': 'Eland - Интернет магазин техники!',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'ИНТЕРНЕТ-МАГАЗИН КОМПЬЮТЕРНОГО ОБОРУДОВАНИЯ',
        'text_on_page': 'Компания Eland – ответственный и надежный поставщик IT оборудования и программного обеспечения на территории Казахстана! '
                        'Основные направления деятельности компании ELand:',

        'paragraphs': [
            'продажа компьютерного оборудования и комплектующих, систем резервного копирования и хранения данных  и программного обеспечения мировых производителей;',
            'поставка многопроцессорных серверов, систем резервного хранения данных  и графических станций любых конфигураций;',
            'поставка широкого ассортимента источников бесперебойного питания и видео наблюдения;',
            'поставка оригинального периферийного и проекционного оборудования, телекоммуникационной и сетевой техники, расходных материалов.'
        ]
    }

    return render(request, 'main/about.html', context)

