# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.
# Внутри каждого представления должна быть переменная html —
# многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.
# Сохраняйте в логи данные о посещении страниц.

from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)
def main_page(request):
    html = """
        <html>
        <head>
        <title>Главная страница</title>
        </head>
        <body>
        <h1>Приветствую Вас на моем сайте!</h1>
        <h2>Устраивайтесь поудобнее! Возможно будет интересно:)</h2>
        <p>Здесь как-будто мелким текстом расписана концепция сайта:)</p>
        </body>
        </html>
        """

    logger.info(f'new visit on my site - main_page')
    return HttpResponse(html)

def about_me(request):
    html = """
        <html>
        <head>
        <title>Обо мне</title>
        </head>
        <body>
        <h1>Основные параметры:</h1>
        <h2>Шутка! :)</h2>
        <p>Здесь должно быть много текста - описания</p>
        </body>
        </html>
        """
    logger.info(f'new visit on my site - page about me')
    return HttpResponse(html)