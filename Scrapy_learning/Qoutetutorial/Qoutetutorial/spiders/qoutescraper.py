import scrapy


class QoutescraperSpider(scrapy.Spider):
    name = "qoutescraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        all_divs = response.css("div.quote")[0]
        title = all_divs.css("span.text::text").extract()
        author = all_divs.css(".author::text").extract()
        tags = all_divs.css(".tag::text").extract()
        # text = response.xpath('//div/span[@class="text"]/text()') # using xpath
        yield{
            "title":title,
            "author":author,
            "tags":tags
        }