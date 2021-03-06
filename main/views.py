from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from scrapyd_api import ScrapydAPI
# connect scrapyd service
scrapyd = ScrapydAPI('http://localhost:6800')
# from scrapy_app.settings import URL_FILES
from scrapy_app.tasks import run_spider
from scrapy_app.utils import get_urls

URL_FILES = ['https://hunter.io/companies/letters/0/1/'
			,'https://hunter.io/companies/letters/1/1/'
			,'https://hunter.io/companies/letters/2/1/'
			,'https://hunter.io/companies/letters/3/1/'
			,'https://hunter.io/companies/letters/4/1/'
			,'https://hunter.io/companies/letters/5/1/'
			,'https://hunter.io/companies/letters/6/1/'
			,'https://hunter.io/companies/letters/7/1/'
			,'https://hunter.io/companies/letters/8/1/'
			,'https://hunter.io/companies/letters/9/1/'
			,'https://hunter.io/companies/letters/a/1/'
			,'https://hunter.io/companies/letters/b/1/'
			,'https://hunter.io/companies/letters/c/1/'
			,'https://hunter.io/companies/letters/d/1/'
			,'https://hunter.io/companies/letters/e/1/'
			,'https://hunter.io/companies/letters/f/1/'
			,'https://hunter.io/companies/letters/g/1/'
			,'https://hunter.io/companies/letters/h/1/'
			,'https://hunter.io/companies/letters/i/1/'
			,'https://hunter.io/companies/letters/j/1/'
			,'https://hunter.io/companies/letters/k/1/'
			,'https://hunter.io/companies/letters/l/1/'
			,'https://hunter.io/companies/letters/m/1/'
			,'https://hunter.io/companies/letters/n/1/'
			,'https://hunter.io/companies/letters/o/1/'
			,'https://hunter.io/companies/letters/p/1/'
			,'https://hunter.io/companies/letters/q/1/'
			,'https://hunter.io/companies/letters/r/1/'
			,'https://hunter.io/companies/letters/s/1/'
			,'https://hunter.io/companies/letters/t/1/'
			,'https://hunter.io/companies/letters/u/1/'
			,'https://hunter.io/companies/letters/v/1/'
			,'https://hunter.io/companies/letters/w/1/'
			,'https://hunter.io/companies/letters/x/1/'
			,'https://hunter.io/companies/letters/y/1/'
			,'https://hunter.io/companies/letters/z/1/']

from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')
scrapyd.schedule('project_name', 'spider_name')
#@csrf_exempt
#@require_http_methods(['POST', 'GET']) # only get and post
def crawl(request):
    scrapyd = ScrapydAPI('http://localhost:6800')
    scrapyd.schedule('scrapy_app', 'hunter')
    return


