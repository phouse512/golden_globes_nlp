import scrapy

from golden_globes_project.items import GoldenGlobesPresenters

class PresenterSpider(scrapy.Spider):
    name = "presenter"
    allowed_domains = ["justjared.com"]
    start_urls = [
        "http://www.justjared.com/2015/01/09/golden-globes-2015-full-presenters-list-announced/"
    ]

    def parse(self, response):
        for sel in response.xpath("//div[@class='entry']/span"):
            item = GoldenGlobesPresenters()
            item['presenter'] = sel.extract()
            print item['presenter']
            yield item
