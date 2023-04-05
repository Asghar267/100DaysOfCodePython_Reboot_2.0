import scrapy


class CoronaviresSpider(scrapy.Spider):
    name = "coronavires"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/coronavirus/#countries"]

    def parse(self, response):
        # link = response.xpath("//td/a[@class='mt_a']/@href").get() # get method got only one item
        # name = response.xpath("//td/a[@class='mt_a']/text()").get()
         for country in response.xpath("//td/a[@class='mt_a']"):
            link = country.xpath(".//@href").get()
            name = country.xpath(".//text()").get()
            # absurl =  "https://www.worldometers.info/coronavirus/"+link # same
            absurl2 = response.urljoin(link) # same



            yield{
                "countryname":name,
                "link":absurl2
            }
         # print(response.xpath("//td/a"))