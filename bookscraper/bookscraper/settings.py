# Scrapy settings for bookscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "bookscraper"

SPIDER_MODULES = ["bookscraper.spiders"]
NEWSPIDER_MODULE = "bookscraper.spiders"

FEEDS = {
    'bookdata.json': {'format': 'json'}
}

import os
from dotenv import load_dotenv
load_dotenv()

SCRAPEOPS_API_KEY = os.getenv('ENV_SCRAPEOPS_API_KEY')
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = os.getenv('ENV_SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT')
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = os.getenv('ENV_SCRAPEOPS_FAKE_USER_AGENT_ENABLED')
SCRAPEOPS_NUM_RESULTS = os.getenv('ENV_SCRAPEOPS_NUM_RESULTS')

SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = os.getenv('ENV_SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT')
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = os.getenv('ENV_SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED')


#WINDOWS
#USER_AGENT = 'Mozilla/5.0 (Linux; Android 16; Pixel 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Mobile Safari/537.36'

#MAC OS
#USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "bookscraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "bookscraper.middlewares.BookscraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# Podemos escoger simular solo el user agent o el browser header completo
DOWNLOADER_MIDDLEWARES = {
#  "bookscraper.middlewares.BookscraperDownloaderMiddleware": 543,
#  "bookscraper.middlewares.ScrapeOpsFakeUserAgentMiddleware": 400,
   "bookscraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware": 400,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "bookscraper.pipelines.BookscraperPipeline": 300,
   "bookscraper.pipelines.SaveToSQLitePipeline": 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
