import scrapy
import re
import datetime

from crawling.items import MovieItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http.request import Request
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class RottenTomatoesSpider(CrawlSpider):

    name = 'rottentomatoes'

    IMAGE_DIR = 'D:\\Users\\Administrator\\gb5566\\django_scrapy\\media\\movie\\images'

    custom_settings = {
        "IMAGES_STORE": IMAGE_DIR
    }

    allowed_domains = ['rottentomatoes.com']

    start_urls = ['https://www.rottentomatoes.com/top/bestofrt/?year=2020', ]
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'

    # def start_requests(self):
    #     yield scrapy.Request(
    #         url='https://www.rottentomatoes.com/top/bestofrt/?year=2020',
    #         headers={'User-Agent': self.user_agent}
    #     )

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="//table[@class='table']/tr/td[3]/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(
            restrict_xpaths="//ul[@class='dropdown-menu']/li/a")),
    )

    # def set_user_agent(self, request, spider):
    #     request.header["User-Agent"] = self.user_agent
    #     return request

    # def parse(self, response):
    #     rows = response.xpath("//table[@class='table']/tr/td[3]/a").extract()
    #     for row in rows:
    #         link = 'https://www.rottentomatoes.com' + row
    #         yield scrapy.Request(url=link, callback=self.parse_item)

    #     yield Request(response.urljoin(response.url), callback=self.parse_item)
    #     base_url = 'https://www.rottentomatoes.com'
    #     yearurls = base_url + response.url
    #     for yearurl in yearurls:
    #         yield Request(response.urljoin(yearurl), callback=self.parse_item)

    # def parse(self, response):
    #     rows = response.xpath("//table[@class='table']/tr/td[3]/a").extract()
    #     for row in rows:
    #         link = 'https://www.rottentomatoes.com' + row
    #         yield scrapy.Request(url=link, callback=self.parse_item)

    # try:
    #     for yearlist in response.xpath("(//*[@class='dropdown-menu'])[4]//a/@href").extract():
    #         rows = response.xpath('//*[@class="table"]/tr/td[3]/a/@href').extract()
    #         for row in rows:
    #             link = 'https://www.rottentomatoes.com' + row
    #             yield scrapy.Request(url=link, callback=self.parse_item)
    # except:
    #     print('There is no more years')

    def parse_item(self, response):
        i = MovieItem()
        i['title'] = response.css(
            'h1.mop-ratings-wrap__title ::text').extract_first()
        i['critics_consensus'] = response.css(
            'p.mop-ratings-wrap__text--concensus ::text').extract()
        i['amount_reviews'] = response.xpath(
            "normalize-space(//small[@class='mop-ratings-wrap__text--small']/text())").extract()
        i['approval_percentage'] = response.xpath(
            "normalize-space((//span[@class='mop-ratings-wrap__percentage'])[1]/text())").extract()
        i['date'] = response.xpath(
            "normalize-space((//div[@class='meta-value']//time)[1]/text())").extract()
        url = response.css('.posterImage ::attr(data-src)').extract()
        link = ''.join(url)
        i['images'] = {link: i['title']}
        return i


# class YahoomovieSpider(CrawlSpider):
#     name = 'yahoomovie'
#     allowed_domains = ['movies.yahoo.com.tw']
#     start_urls = ['https://movies.yahoo.com.tw/chart.html?cate=year', ]

#     IMAGE_DIR = 'D:\\Users\\Administrator\\gb5566\\django_scrapy\\media\\movie\\images\\yahoo'

#     custom_settings = {
#         "IMAGES_STORE": IMAGE_DIR
#     }

#     rules = (
#         Rule(LinkExtractor(
#             restrict_xpaths="(//div[@class='rank_list table rankstyle1']/div[@class='tr'])/div[@class='td']//a"), callback='parse_item', follow=True),
#     )

#     def parse_item(self, response):
#         i = MovieItem()
#         i['title']: response.xpath(
#             "//div[@class='movie_intro_info_r']/h1/text()").extract()
#         i['date']: response.xpath(
#             "//div[@class='movie_intro_info_r']/span/text()").extract_first()
#         i['imdbranking']: response.xpath(
#             "//div[@class='movie_intro_info_r']/span[4]/text()").extract()
#         i['amount_reviews']: response.xpath(
#             "//div[@class='score_num count']/text()").extract()
#         i['images']: response.xpath(
#             "//div[@class='movie_intro_foto']/img/@src").extract()
#         i['critics_consensus']: response.xpath(
#             "normalize-space(//span[@id='story']/text())").extract_first()
#         i['approval_percentage']: response.xpath(
#             "//div[@class='circlenum']/div/span/text()").extract()
#         return i
#         # item = {}
#         #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
#         #item['name'] = response.xpath('//div[@id="name"]').get()
#         #item['description'] = response.xpath('//div[@id="description"]').get()
#         # yield{
#         #     'title': response.xpath(
#         #         "//div[@class='movie_intro_info_r']/h1/text()").extract(),
#         #     'date': response.xpath(
#         #         "//div[@class='movie_intro_info_r']/span/text()").extract_first(),
#         #     'imdbranking': response.xpath(
#         #         "//div[@class='movie_intro_info_r']/span[4]/text()").extract(),
#         #     'amount_reviews': response.xpath(
#         #         "//div[@class='score_num count']/text()").extract(),
#         #     'images': response.xpath(
#         #         "//div[@class='movie_intro_foto']/img/@src").extract(),
#         #     'critics_consensus': response.xpath(
#         #         "normalize-space(//span[@id='story']/text())").extract_first(),
#         #     'approval_percentage': response.xpath(
#         #         "//div[@class='circlenum']/div/span/text()").extract(),
#         # }


# configure_logging()
# runner = CrawlerRunner()


# @defer.inlineCallbacks
# def crawl():
#     yield runner.crawl(RottenTomatoesSpider)
#     yield runner.crawl(YahoomovieSpider)
#     reactor.stop()


# crawl()
# reactor.run()  # the script will block here until the last crawl call is finished
