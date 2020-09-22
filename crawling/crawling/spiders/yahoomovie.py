import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawling.items import MovieItem


class YahoomovieSpider(CrawlSpider):
    name = 'yahoomovie'
    allowed_domains = ['movies.yahoo.com.tw']
    start_urls = ['https://movies.yahoo.com.tw/chart.html?cate=year', ]

    IMAGE_DIR = 'D:\\Users\\Administrator\\gb5566\\django_scrapy\\media\\movie\\images\\yahoo'

    custom_settings = {
        "IMAGES_STORE": IMAGE_DIR
    }

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="(//div[@class='rank_list table rankstyle1']/div[@class='tr'])/div[@class='td']//a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MovieItem()
        i['title']: response.xpath(
            "//div[@class='movie_intro_info_r']/h1/text()").extract()
        i['date']: response.xpath(
            "//div[@class='movie_intro_info_r']/span/text()").extract_first()
        i['imdbranking']: response.xpath(
            "//div[@class='movie_intro_info_r']/span[4]/text()").extract()
        i['amount_reviews']: response.xpath(
            "//div[@class='score_num count']/text()").extract()
        i['images']: response.xpath(
            "//div[@class='movie_intro_foto']/img/@src").extract()
        i['critics_consensus']: response.xpath(
            "normalize-space(//span[@id='story']/text())").extract_first()
        i['approval_percentage']: response.xpath(
            "//div[@class='circlenum']/div/span/text()").extract()
        return i
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # yield{
        #     'title': response.xpath(
        #         "//div[@class='movie_intro_info_r']/h1/text()").extract(),
        #     'date': response.xpath(
        #         "//div[@class='movie_intro_info_r']/span/text()").extract_first(),
        #     'imdbranking': response.xpath(
        #         "//div[@class='movie_intro_info_r']/span[4]/text()").extract(),
        #     'amount_reviews': response.xpath(
        #         "//div[@class='score_num count']/text()").extract(),
        #     'images': response.xpath(
        #         "//div[@class='movie_intro_foto']/img/@src").extract(),
        #     'critics_consensus': response.xpath(
        #         "normalize-space(//span[@id='story']/text())").extract_first(),
        #     'approval_percentage': response.xpath(
        #         "//div[@class='circlenum']/div/span/text()").extract(),
        # }

        # print(item)
