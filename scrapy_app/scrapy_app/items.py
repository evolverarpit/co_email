# -*- coding: utf-8 -*-

from __future__ import absolute_import
#from main2.models import HunterItemBaba,SourceItemBaba,Comp,Hont
import json
import scrapy
#from scrapy_djangoitem import DjangoItem
import os
import unittest

from scrapy_djangoitem import DjangoItem, Field
class CompanyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    employees = scrapy.Field(serializer=list)
#class CompanyItem(DjangoItem):
    #django_model = Comp
#class HunterItem(DjangoItem):
    #django_model = Hont
class HunterItem(scrapy.Item):
    name = scrapy.Field()
    email = scrapy.Field()
    pattern = scrapy.Field()
    sources = scrapy.Field()
    html = scrapy.Field()

class SourceItem(scrapy.Item):
    url = scrapy.Field()
    emails = scrapy.Field(serializer=list)
    links = scrapy.Field(serializer=list)
    html = scrapy.Field()
