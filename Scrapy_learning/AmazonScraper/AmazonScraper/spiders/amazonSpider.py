import scrapy
from requests import Request

from ..items import AmazonscraperItem

class AmazonspiderSpider(scrapy.Spider):
    name = "amazonSpider"
    allowed_domains = ["www.amazon.com"]
    start_urls = [
        "https://www.amazon.com/s?bbn=283155&rh=p_n_publication_date%3A1250226011&dc&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0"]

    CUSTOM_PROXY = []


    def parse(self, response):
        print(response)
        print("\n")
        items = AmazonscraperItem()
        book_name = response.css(".a-size-base-plus::text").extract()

        book_author = response.css(".a-color-secondary .a-size-base.s-link-style").css('::text').extract()
        book_price = response.css(".a-price span span").css('::text').extract()
        book_imagelink = response.css(".s-image::attr(src)").extract()

        items["book_name"] = book_name
        items["book_author"] = book_author
        items["book_price"] = book_price
        items["book_imagelink"] = book_imagelink
        print(book_name, book_author, book_price, book_imagelink)
        print("\n")
        yield items

