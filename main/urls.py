# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^crawl/', views.crawl, name='crawl'),
]



