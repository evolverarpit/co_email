# coding=utf-8
from __future__ import absolute_import

from celery import Celery
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
app = Celery('hunter', broker=settings['CELERY_BROKER'], backend=settings['CELERY_BACKEND'], include=['scrapy_app.tasks'])
