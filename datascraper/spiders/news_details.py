from itertools import count
import json
from ntpath import join
from turtle import title
import scrapy
# from spiders.news_details import DatascraperItem
from datascraper.items import DatascraperItem
from scrapy.spiders import CrawlSpider
from scrapy.crawler import CrawlerProcess
# from pathlib import Path

# parent = Path(__file__).parent
# file_path = parent / 'github.json'

class News_Detail(scrapy.Spider):
    name = 'punchng'
    allowed_domain = ['punchng.com']
    start_urls = ['http://punchng.com']

    def parse(self, response):
        # url = 'http://punchng.com'
        data = DatascraperItem()

        # data['title'] = response.css('li.new-item a::text').getall()
        # data['news_link'] = url + response.css('li.new-item a::attr(href)').getall()
        # yield data
        for data in response.css('div.just-in-timeline'):
            yield ({
                'title': data.css('li.new-item a::text').getall(),
               'news_link': data.css('li.new-item a::attr(href)').getall()
            })
       
        # yield scrapy.Request(news_link, callback=self.parse)

        # title_list = response.xpath('//*li[@class="new-item"]/h3[@class"entry-title"]/a/text()').extract()
        # news_link_list = response.xpath('//*li[@class="new-item"]/h3[@class"entry-title"]/a/@href').extract()

        # # count = len(title_list)

        # # for i in range(0, count):

        #     details = DatascraperItem()

        #     details['title'] = title_list[i]
        #     details['news_link'] = url + news_link_list[i]

        #     print(title_list[i], (url + news_link_list[i]))

        #     yield details


      

    # for timeline in response.xpath('//div[@class"just-in-timeline"]'):

    #     yield {'title': timeline.xpath('.//a/text()').extract()}

    # news_link = response.xpath('//li[@class="new-item"]/h3[@class"entry-title"]/a/@href').extract()
    # yield scrapy.Request(response.urljoin(news_link))

    # for timeline in response.xpath('//li[@class="new-item"]/h3[@class"entry-title"]/a/text()').extract():
    #     yield {"title": timeline}

    # for href in response.xpath('//li[@class="new-item"]/h3[@class"entry-title"]/a/@href').extract():
    #     yield scrapy.Request(response.urljoin(href), self parse)
