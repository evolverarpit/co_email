# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_app project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os
import sys

# DJANGO INTEGRATION

sys.path.append(os.path.dirname(os.path.abspath('.')))
# Do not forget the change iCrawler part based on your project name
os.environ['DJANGO_SETTINGS_MODULE'] = 'iCrawler.settings'

# import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env'
dir_path = os.path.dirname(os.path.realpath(__file__))
try:
    load_dotenv(dotenv_path=env_path)
except:
    load_dotenv(dotenv_path=dir_path + '/.env')
# This is required only if Django Version > 1.8
import django
django.setup()
BOT_NAME = 'scrapy_app'

SPIDER_MODULES = ['scrapy_app.spiders']
NEWSPIDER_MODULE = 'scrapy_app.spiders'
LOG_ENABLED = True
LOG_FILE = './log'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_app (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_app.middlewares.ScrapyAppSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_app.middlewares.ScrapyAppDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scrapy_app.pipelines.ScrapyAppPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'hunter.middlewares.HunterSpiderMiddleware': 543,
# }
# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
    'scrapy_app.middlewares.HunterDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'hunter.pipelines.HunterPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
ITEM_PIPELINES = {
    'scrapy_app.pipelines.HunterMongoPipeline': 300,
    'scrapy_app.pipelines.SourcesMongoPipeline': 301
}

MONGODB_SERVER = os.getenv('MONGO_SERVER', 'localhost')
MONGODB_PORT = os.getenv('MONGO_PORT', 27017)
MONGODB_DB = os.getenv('MONGO_DB', 'co-emails')
MONGODB_HUNTER_COLLECTION = os.getenv('MONGO_HUNTER_COLLECTION', 'companies')
MONGODB_SOURCES_COLLECTION = os.getenv('MONGO_SOURCES_COLLECTION', 'sources')
MONGODB_LINKS_COLLECTION = os.getenv('MONGO_LINKS_COLLECTION', 'links')
CELERY_BROKER = os.getenv('CELERY_BROKER', 'amqp://guest@127.0.0.1//')
CELERY_BACKEND = os.getenv('CELERY_BACKEND', 'rpc://')
PROXIES = [
    'http://51.15.197.135:60000',
    'http://51.15.197.135:60001',
    'http://51.15.197.135:60002'
]
# PROXIES = None  # set to none to remove proxy capability
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile'
    ' Safari/537.36 Edge/15.15254',
    'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056)'
    'AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile '
    'Safari/537.36 Edge/12.10536',
    'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 '
    'Chrome/52.0.2743.98 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) '
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/60.0.3112.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
    'like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 '
    '(KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 '
    'Firefox/15.0.1',
    'Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 ('
    'KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED)'
    ' AppleWebKit/537.36 ('
    'KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'

]

URL_FILES = [
    dir_path + '/urls_all.txt',
]
# set to none to get all links in a page
COMPANY_LIMIT = os.getenv('COMPANY_LIMIT', None)
# set to none to get all source links
SOURCE_LIMIT = os.getenv('SOURCE_LIMIT', None)

if COMPANY_LIMIT:
    COMPANY_LIMIT = int(COMPANY_LIMIT)
if SOURCE_LIMIT:
    SOURCE_LIMIT = int(SOURCE_LIMIT)
if MONGODB_PORT:
    MONGODB_PORT = int(MONGODB_PORT)