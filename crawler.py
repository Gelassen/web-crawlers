import requests
from lxml import html
from store_item import StoreItem
from tqdm import tqdm 
import pandas as pd

HOME_PAGE = "https://slickdeals.net/computer-deals/?page=1"

class Crawler:

    def __init__(self):
        self.li_xpath = "//li[contains(@class, 'bp-p-blueberryDealCard bp-p-filterGrid_item bp-p-dealCard bp-c-card')]"  # Choose the `li` items

        self.names_xpath = ".//a[@class='bp-c-card_title bp-c-link']/text()"
        self.manufacturer_xpath = ".//*[contains(@class, 'bp-c-card_subtitle')]/text()"
        self.price_xpath = ".//*[contains(@class, 'bp-p-dealCard_price')]/text()"
    
    def get_source(self, page_url):
        """
        A function to download the page source of the given URL.
        """
        r = requests.get(page_url)
        source = html.fromstring(r.content)

        return source

    def get_data(self, source):
        li_list = source.xpath(self.li_xpath)
        item_names = [
            li.xpath(self.names_xpath) for li in li_list
        ]
        print("Items in source")
        print(len(item_names))
        return li_list

    def scrap(self):
        source = self.get_source(HOME_PAGE)
        li_list = self.get_data(source)
        items = list()
        for li in li_list:
            name = li.xpath(self.names_xpath)
            manufacturer = li.xpath(self.manufacturer_xpath)
            price = li.xpath(self.price_xpath)
            
            print(name)
            
            # Store inside a class
            item = StoreItem(name, price, manufacturer)
            items.append(item) 
        return items

    def scrap(self, pages):
        items = list()
        for num in tqdm(range(1, pages)):
            url = f"https://slickdeals.net/computer-deals/?page={num}"
            source = self.get_source(url)  # Get HTML code

            li_list = source.xpath(self.li_xpath)

            for li in li_list:
                # clean_text(li.xpath(self.names_xpath))
                name = li.xpath(self.names_xpath)
                manufacturer = li.xpath(self.manufacturer_xpath)
                price = li.xpath(self.price_xpath)

                print(name)

                # Store inside a class
                item = StoreItem(name, price, manufacturer)
                items.append(item)
        return items
    
    def print_results(self, items):
        df = pd.DataFrame(
            {
                "name": [item.name for item in items],
                "price": [item.price for item in items],
                "manufacturer": [item.manufacturer for item in items],
            }
        )

        df.head()

crawler = Crawler()
result = crawler.scrap(2)
# table = crawler.print_results(result)

# print(result)
# print(table)