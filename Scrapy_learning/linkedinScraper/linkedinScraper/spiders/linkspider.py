import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider"
    allowed_domains = ["www.linkedin.com"]
    start_urls = ["http://www.linkedin.com/"]

    def parse(self, response):
        pass
