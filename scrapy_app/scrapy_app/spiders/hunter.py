# coding=utf-8
# !/usr/bin/env python3
from __future__ import absolute_import
import json
import psycopg2
#from main2.models import HunterItemBaba,SourceItemBaba,Comp,Hont,CompanyItemBaba
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy_app.items import (CompanyItem, HunterItem)
from scrapy_app.settings import SOURCE_LIMIT, COMPANY_LIMIT, PROXIES, USER_AGENT_LIST
from scrapy_app.utils import get_email


class Hunter(scrapy.Spider):
    """Hunter.io scraper"""


    name = 'hunter'
    def start_requests(self):
        urls = ['https://hunter.io/companies/letters/0/1/','https://hunter.io/companies/letters/1/1/','https://hunter.io/companies/letters/2/1/','https://hunter.io/companies/letters/3/1/','https://hunter.io/companies/letters/4/1/','https://hunter.io/companies/letters/5/1/','https://hunter.io/companies/letters/6/1/','https://hunter.io/companies/letters/7/1/','https://hunter.io/companies/letters/8/1/','https://hunter.io/companies/letters/9/1/','https://hunter.io/companies/letters/a/1/','https://hunter.io/companies/letters/b/1/','https://hunter.io/companies/letters/c/1/','https://hunter.io/companies/letters/d/1/','https://hunter.io/companies/letters/e/1/','https://hunter.io/companies/letters/f/1/','https://hunter.io/companies/letters/g/1/','https://hunter.io/companies/letters/h/1/','https://hunter.io/companies/letters/i/1/','https://hunter.io/companies/letters/j/1/','https://hunter.io/companies/letters/k/1/','https://hunter.io/companies/letters/l/1/','https://hunter.io/companies/letters/m/1/','https://hunter.io/companies/letters/n/1/','https://hunter.io/companies/letters/o/1/','https://hunter.io/companies/letters/p/1/','https://hunter.io/companies/letters/q/1/','https://hunter.io/companies/letters/r/1/','https://hunter.io/companies/letters/s/1/','https://hunter.io/companies/letters/t/1/','https://hunter.io/companies/letters/u/1/','https://hunter.io/companies/letters/v/1/','https://hunter.io/companies/letters/w/1/','https://hunter.io/companies/letters/x/1/','https://hunter.io/companies/letters/y/1/','https://hunter.io/companies/letters/z/1/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        no_of_pages = Selector(response).xpath('/html/body/section/div/div/div/a/text()').extract()[-1]
        try:
            no_of_pages = int(no_of_pages)
            for page in list(range(1, no_of_pages + 1)):
                if page != 1:
                    yield scrapy.Request(url=response.url.replace(str(1), str(page)), callback=self.get_page)
                else:
                    yield scrapy.Request(url=response.url, callback=self.get_page)
        except ValueError:
            yield scrapy.Request(url=response.url, callback=self.get_page)

    def get_page(self, response):
        extractor = LinkExtractor(
            restrict_css='section.company-list a.blue-link', deny='/letters/')
        companies = extractor.extract_links(response=response)
        for co in companies[:COMPANY_LIMIT]:
            yield scrapy.Request(url=co.url, callback=self.get_sources, meta={'company_url': co.text.strip()})

    def get_sources(self, response):
        try:
            results = Selector(response).xpath(
                '/html/body/div[1]/div/div[3]').css('div.result')
            try:
                pattern = Selector(response).xpath(
                    '/html/body/div[1]/div/div[2]/strong/text()').extract_first().strip()
            except:
                pattern = None
            url = response.meta.get('company_url')
            company = CompanyItem()
            #import pdb;pdb.set_trace()
            company['name'] = Selector(response).xpath(
                '/html/body/div[1]/div/div[1]/h1/text()').extract_first().strip()
            company['url'] = url
            company['employees'] = []

            for email in results:
                email_to_search = None
                try:
                    email_to_search = self.cfDecodeEmail(
                        email.css('div.email a::attr(data-cfemail)').extract_first())
                except:
                    pass
                item = HunterItem()
                item['name'] = email.css('span.name::text').extract_first() or None
                item['sources'] = email.css('div.sources-list a::attr(href)').extract()[:SOURCE_LIMIT]  # get max of 3 links
                item['email'] = get_email(item['sources'], url, email_to_search)
                item['pattern'] = pattern or self.get_pattern(item, url)
                item['html'] = email.extract()
                company['employees'].append(item)
                name11 = email.css('span.name::text').extract_first() or None
                sources11 = email.css('div.sources-list a::attr(href)').extract()[:SOURCE_LIMIT]  # get max of 3 links
                email11 = get_email(sources11, url, email_to_search)
                pattern11 = pattern or self.get_pattern(item, url)
                html11 = email.extract()
                conn = psycopg2.connect(host="localhost",database="coemail", user="postgres", password="postgres")
                query = "select url from main2_hunteritemnew where name='" + name11 + "',email='"+email11+"',pattern='"+pattern11+"',sources='"+sources11+"';"
                cur = conn.cursor()
                cur.execute(query)
                if not cur.fetchall():
                    cur.execute("insert into main2_hunteritemnew(name,email,pattern,sources,html) values('"+name11+ "', '"+email11+"','"+pattern11+"','"+sources11+"','"+html11+"',);")
                    #cur.execute("insert into main2_hunteritemnew(name,email,pattern,sources,html) values('"+item['name']+ "', '"+item['email']+"','"+item['pattern']+"','"+item['sources']+"','"+item['html']+"',);")
                cur.close()
                conn.close()
            data = dict(company)
            data['_id'] = url
            conn = psycopg2.connect(host="localhost",database="coemail", user="postgres", password="postgres")
            query = "select url from main2_companyitemnew where url='" + url + "';"
            cur = conn.cursor()
            cur.execute(query)
            if cur.fetchall():
                cur.execute("update main2_companyitemnew set name = '"+company['name']+"', employees = '"+json.dumps(company['employees'])+"' where url='"+url+"';")
               
                conn.commit()
            else:
                cur.execute("insert into main2_companyitemnew(name,url,employees) values('"+company['name']+ "', '"+url+"','"+json.dumps(json.dumps(company['employees']))+"');")
                #cur.execute("insert into main2_companyitembaba(url,data) values('"+url+"','"+json.dumps(json.dumps(data))+"');")
                conn.commit()
            cur.close()
            conn.close()
            print('************************')
            print('************************')
            print('************************')
            yield company
        except AttributeError as e:
            print(str(e.args))

    def cfDecodeEmail(self, encodedString):
        r = int(encodedString[:2], 16)
        email = ''.join([chr(int(encodedString[i:i + 2], 16) ^ r)
                         for i in range(2, len(encodedString), 2)])
        return email


    def get_pattern(self, item, url):
        if item['name'] and item['email']:
            email = item['email'].split('@')
            name = item['name'].lower()
            name = name.split(' ')
            if len(email) == 2:
                email = email[0].split('.')
                if len(email) == 2:
                    if len(name) == 2:
                        if email[0] == name[0] and email[1] == name[1]:
                            return '{{first_name}}.{{last_name}}@{0}'.format(url)
                        elif email[0] == name[1] and email[1] == name[0]:
                            return '{{last_name}}.{{first_name}}@{0}'.format(url)
                        elif email[0] == name[0][0] and email[1] == name[1]:
                            return '{{f}}.{{last_name}}@{0}'.format(url)
                        elif email[0] == name[0] and email[1] == name[0][0]:
                            return '{{first_name}}.{{l}}@{0}'.format(url)
                elif len(email) == 1:
                    email = email[0]
                    email = email.replace(name[0], 'first')
                    # make sure last has same no of chars as first
                    email = email.replace(name[1], '.last')
                    if email.find('first') == 0 and email.find('.last') == 5:
                        return '{{first_name}}{{last_name}}@{0}'.format(url)
                    elif email.find('first') == -1 and email.find('.last') == 1:
                        return '{{f}}{{last_name}}@{0}'.format(url)
                    elif email.find('first') == -1 and email.find('.last') == 0:
                        return '{{last_name}}@{0}'.format(url)
                    elif email.find('first') == 0 and email.find('.last') == -1:
                        if email.find('first') == 0 and email.find('.') == -1:
                            return '{{first_name}}@{0}'.format(url)
                        return '{{first_name}}{{l}}@{0}'.format(url)
        return None
