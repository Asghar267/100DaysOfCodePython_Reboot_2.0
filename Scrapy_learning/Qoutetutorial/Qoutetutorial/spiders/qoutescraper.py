import scrapy
from ..items import QoutetutorialItem

class QoutescraperSpider(scrapy.Spider):
    name = "qoutescraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        all_divs = response.css("div.quote")
        items = QoutetutorialItem()
        for qoutes in all_divs:
            title = qoutes.css("span.text::text").extract()
            author = qoutes.css(".author::text").extract()
            tag = qoutes.css(".tag::text").extract()
            # text = response.xpath('//div/span[@class="text"]/text()') # using xpath
            print()
            items["title"] =title
            items["author"] =author
            items["tag"] =tag
            # yield{
            #     "title":title,
            #     "author":author,
            #     "tags":tag
            # }

            yield items

            next_page = response.css("li.next a::attr(href)").get()
            print(next_page)
            if next_page is not None:
                yield response.follow(next_page,callback =self.parse)