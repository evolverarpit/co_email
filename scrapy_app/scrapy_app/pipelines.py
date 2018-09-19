# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import json
# class ScrapyAppPipeline(object):
#     def process_item(self, item, spider):
#         return item


# -*- coding: utf-8 -*-
from __future__ import absolute_import

# import pymongo
# from hunter.settings import (MONGODB_DB, MONGODB_HUNTER_COLLECTION, MONGODB_PORT, MONGODB_SERVER,
                             # MONGODB_SOURCES_COLLECTION)






from main2.models import HunterItemBaba,SourceItemBaba
import json



class HunterMongoPipeline:

    def __init__(self):
    	pass

    def process_item(self, company, spider):
    	data = dict(company)
        data['_id'] = data.pop('url')  # make company url to be id
        url = HunterItemBaba.object.filter(url=data.pop('url'))
        if url:
        	url[0].data = json.dumps(data)
        	#url[0].save()
        else:
                pass
	        #HunterItemBaba.object.create(url=data.pop('url'),data=json.dumps(data))
        return 'saved {} successfully to companies'.format(data['_id'])


class SourcesMongoPipeline:

    def __init__(self):
    	pass

    def process_item(self, source, spider):
        data = dict(source)
        data['_id'] = data.pop('url')  # make company url to be id
        url = SourceItemBaba.object.filter(url=data.pop('url'))
        if url:
        	url[0].data = json.dumps(data)
        	#url[0].save()
        else:
                pass
	        #SourceItemBaba.object.create(url=data.pop('url'),data=json.dumps(data))
        return 'saved {} successfully to sources'.format(data['_id'])

