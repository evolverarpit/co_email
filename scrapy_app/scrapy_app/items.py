# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    employees = scrapy.Field(serializer=list)


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
