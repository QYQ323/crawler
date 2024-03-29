# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import ExampleItem

class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/examples/index.html']

    def parse(self, response):
        le=LinkExtractor(restrict_css='div.toctree-wrapper.compound li.toctree-l2')

        print(len(le.extract_links(response)))
        for link in le.extract_links(response):
            yield scrapy.Request(link.url,callback=self.parse_example)

    def parse_example(self,response):
        example = ExampleItem()
        href = response.css('a.reference.external::attr(href)').extract_first()
        url = response.urljoin(href)
        example['file_urls']=[url]
        return example