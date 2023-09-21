import scrapy 

class HHSpider(scrapy.Spider):
    name = 'hh-spider'
    start_urls = [
        'https://hh.ru/search/vacancy?area=1&ored_clusters=true&professional_role=96&search_period=30&text=Android&order_by=publication_time'
        ]

    def __init__(self):
        self.BASE_URL = 'https://hh.ru'
        self.JOB_SELECTOR = '.vacancy-serp-item-body'
        self.JOB_TITLE_SELECTOR = '.serp-item__title::text'
        self.JOB_COMPANY_SELECTOR = '.bloko-link_kind-tertiary::text'
        self.JOB_COMPANY_URL_SELECTOR = '.bloko-link_kind-tertiary::attr(href)'
        self.JOB_COMPENSATION_SELECTOR = '.bloko-header-section-2::text'
        self.NEXT_SELECTOR = '.bloko-button.pager-next::attr(href)'

    def parse(self, response):
        for vacancy in response.css(self.JOB_SELECTOR): 
            yield {
                'jobTitle' : vacancy.css(self.JOB_TITLE_SELECTOR).get(),
                'compensation' : vacancy.css(self.JOB_COMPENSATION_SELECTOR).get(),
                'company' : vacancy.css(self.JOB_COMPANY_SELECTOR).get(),
                'companyUrl' : self.BASE_URL + vacancy.css(self.JOB_COMPANY_URL_SELECTOR).get()
            }
        
        next_page = response.css(self.NEXT_SELECTOR).get()
        print("Next page: " + response.urljoin(next_page))
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page))

