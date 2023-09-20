import scrapy 

class HHSpider(scrapy.Spider):
    name = 'hh-spider'
    start_urls = [
        'https://belgorod.hh.ru/search/vacancy?area=1&ored_clusters=true&professional_role=96&search_period=30&text=Android&order_by=publication_time'
        ]

    def parse(self, response):
        JOB_TITLE_SELECTOR = '.serp-item__title::text'

        for title in response.css(JOB_TITLE_SELECTOR): 
            yield {
                'jobTitle' : title.get()
            }