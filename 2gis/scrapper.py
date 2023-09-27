import scrapy 

class TwoGisSpider(scrapy.Spider):

    name = '2gis-spider'
    start_urls = [
        'https://2gis.ru/spb/search/IT%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8?m=30.313803%2C59.944294%2F11'
    ]

    def __init__(self):
        self.BASE_URL = "https://2gis.ru"
        self.PLACES_SELECTOR = "._awwm2v" # redundant
        self.PLACE_SELECTOR = "._1kf6gff"
        self.PLACE_TITLE_SELECTOR = "._1al0wlf::text"
        self.PLACE_ADDRESS_SELECTOR = "._klarpw::text"
        self.PLACE_PAGINATION_URL = "https://2gis.ru/spb/search/IT%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8/page/{0}?m=30.32087%2C59.986787%2F12.3"
        # pagination
        # https://2gis.ru/spb/search/IT%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8/page/4?m=30.32087%2C59.986787%2F12.3

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url = url,
                callback = self.parse,
                headers = { "User-Agent": self.name + " https://github.com/Gelassen/web-crawlers" }
            )  

    def parse(self, response):
        for place in response.css(self.PLACE_SELECTOR):
            yield {
                "place" : place.css(self.PLACE_TITLE_SELECTOR),
                "address" : place.css(self.PLACE_ADDRESS_SELECTOR)
            }

        # next page works very tricky:
        # - the selector have to rely on class which is not unique and may reflect previous or next button
        # - pagination url is not stable, you can not iterate over array of pages indexes

        # scrapy docs covers some hints how to handle this and similar cases 
