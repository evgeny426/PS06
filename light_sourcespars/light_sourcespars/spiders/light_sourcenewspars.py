import scrapy
import csv


class LightSourcenewsparsSpider(scrapy.Spider):
    name = "light_sourcenewspars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        light_sources = response.css('div._Ud0k')
        for light_source in light_sources:
            yield {
                'name': light_source.css('div.lsooF span::text').get(),
                'price': light_source.css('div.pY3d2 span::text').get(),
                'url': response.urljoin(light_source.css('a').attrib['href'])
            }


    def close(self, reason):
        with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Цена', 'Ссылка'])
            for item in self.crawler.stats.get_value('item_scraped_count'):
                writer.writerow([item['name'], item['price'], item['url']])
