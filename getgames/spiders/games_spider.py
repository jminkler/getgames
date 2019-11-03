import scrapy
import urlparse
import os.path
from os import path

from scrapy.http import Request


class GamesSpider(scrapy.Spider):
    name = "games"
    allowed_domains = ["theweekinchess.com"]
    start_urls = ['https://theweekinchess.com/a-year-of-pgn-game-files']

    def parse(self, response):
        for href in response.css('.calendar-table a[href$=".pgn"]::attr(href)').extract():
            fname = "pgn/" + response.urljoin(href)
            if not path.exists(fname):
                self.logger.info('Crawling PGN %s', fname)
                yield Request(
                    url=response.urljoin(href),
                    callback=self.save_pdf
                )

    def save_pdf(self, response):
        fpath = response.url.split('/')[-1]
        fname = "pgn/" + fpath
        if not path.exists(fname):
            self.logger.info('Saving PGN %s', fname)
            with open(fname, 'wb') as f:
                f.write(response.body)
