import scrapy 

# https://hh.ru/robots.txt deny usage of all robots except from popular search engines
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
        self.NEXT_SELECTOR = '.bloko-button[data-qa="pager-next"]::attr(href)'

    def start_requests(self):
        for url in self.start_urls:
            # proxy = 'https://95.56.254.139:3128'
            yield scrapy.Request(url=url, 
                callback=self.parse, 
                headers={"User-Agent": "hh-crawler (+https://github.com/Gelassen/web-crawlers)"},
            )

    def parse(self, response):
        for vacancy in response.css(self.JOB_SELECTOR): 
            yield {
                'jobTitle' : vacancy.css(self.JOB_TITLE_SELECTOR).get(),
                'compensation' : ''.join(vacancy.css(self.JOB_COMPENSATION_SELECTOR).getall()),
                'company' : ''.join(vacancy.css(self.JOB_COMPANY_SELECTOR).getall()),
                'companyUrl' : self.BASE_URL + vacancy.css(self.JOB_COMPANY_URL_SELECTOR).get()
            }

        next_page = response.css(self.NEXT_SELECTOR).get()

        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page))
