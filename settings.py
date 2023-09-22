# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1
# }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "job_boards_crawler (+https://github.com/Gelassen/web-crawlers)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

FEED_EXPORT_ENCODING = "utf-8"

DOWNLOAD_DELAY = 5.0