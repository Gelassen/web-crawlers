import scrapy

# // https://www.stepstone.de/work/android-softwareentwickler
# // https://www.stepstone.de/work/android-software-engineer

class StepStoneSpider(scrapy.Spider):
    name = 'stepstone-spider'
    start_urls = [
        # 'https://www.stepstone.de/work/android-softwareentwickler',
        'https://www.stepstone.de/work/android-software-engineer'
    ]


    def __init_(self):
        self.BASE_URL = 'https://www.stepstone.de'
        self.JOB_SELECTOR = '.res-1xbm2ji'
        self.JOB_TITLE_SELECTOR = '.res-1uowbrp::text'
        self.JOB_COMPANY_SELECTOR = '.res-zmp0rg::text' # '.res-1lxoyqq::text'
        self.JOB_COMPANY_URL_SELECTOR = '.res-fr75pv::attr(href)'
        self.JOB_COMPENSATION_SELECTOR = ''
        self.JOB_LOCATION_SELECTOR = '.res-zmp0rg::text' 
        self.NEXT_SELECTOR = '.res-1w7ajks[aria-label="Next"]::attr(href)'
        self.NEXT_SELECTOR_DISABLED = '.res-1w7ajks[disabled=""]'

    def parse(self, response): 
        for vacancy in response.css(self.JOB_SELECTOR): 
            yield {
                'jobTitle' : vacancy.css(self.JOB_TITLE_SELECTOR).get(),
                'company' : vacancy.css(self.JOB_COMPANY_SELECTOR).get(),
                'location' : vacancy.css(self.JOB_LOCATION_SELECTOR).get(),
                'companyUrl' : vacancy.css(self.JOB_COMPANY_URL_SELECTOR).get()
            }

        next_page = response.css(self.NEXT_SELECTOR).get()
        next_page_disabled = response.css(self.NEXT_SELECTOR_DISABLED).get()
        
        if next_page_disabled is not None:
            yield scrapy.Request(next_page)