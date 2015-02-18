import scrapy

from golden_globes_project.items import GoldenGlobesNomineesItem, GoldenGlobesPresenters

class DmozSpider(scrapy.Spider):
    name = "globe"
    allowed_domains = ["goldenglobes.com"]
    start_urls = [
        "http://www.goldenglobes.com/2015_72nd_Golden_Globes_Nominees"
    ]

    def parse(self, response):
        for sel in response.xpath("//div[re:test(@class, 'view-AwardsView')]/div[re:test(@class, 'view-content')]/div[re:test(@class, 'views-row')]"):
            item = GoldenGlobesNomineesItem()
            item['award_name'] = sel.xpath("table/tr/div[re:test(@class, 'views-field-title')]/text()").extract()
            item['nominee_1'] = sel.xpath("table/tr/td[1]/div[@class='views-info-wrapper']/div[@class='views-info']/div/a/text()").extract()
            item['nominee_2'] = sel.xpath("table/tr/td[2]/div[@class='views-info-wrapper']/div[@class='views-info']/div/a/text()").extract()
            item['nominee_3'] = sel.xpath("table/tr/td[3]/div[@class='views-info-wrapper']/div[@class='views-info']/div/a/text()").extract()
            item['nominee_4'] = sel.xpath("table/tr/td[4]/div[@class='views-info-wrapper']/div[@class='views-info']/div/a/text()").extract()
            item['nominee_5'] = sel.xpath("table/tr/td[5]/div[@class='views-info-wrapper']/div[@class='views-info']/div/a/text()").extract()
            yield item
