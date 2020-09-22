import scrapy
import os
import re
from movie.models import Movie
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from datetime import datetime


def clean_title(param):
    return param


def clean_critics_consensus(param):
    param = ' '.join(param)
    return param


def clean_date(param):
    regex = '[^A-Za-z0-9]+'  # anything that's NOT a-z, A-Z, 0-9
    datevalue = [re.sub(regex, '', str(i)) for i in param]

    for date in datevalue:
        param = datetime.strptime(date, "%b%d%Y").strftime("%Y-%m-%d")
    return param
    # try:
    #     x = re.sub(regex, '', str(date))
    #     datetrn = x[5:]
    #     param = datetime.strptime(datetrn, "%Y%m%d").strftime("%Y-%m-%d")
    #     return param
    # except ValueError:
    #     # x = re.sub(regex, ' ', str(date))
    #     # param = datetime.strptime(date, "%b %d %Y").strftime("%Y-%m-%d")
    #     return param

    # if datevalue == datetime.strptime(datevalue, "%Y%m%d"):
    #         # datetrn = date[5:]
    #         param = datetime.strptime(datevalue, "%Y%m%d").strftime("%Y-%m-%d")
    #         return param
    # else:
    #     param = datetime.strptime(datevalue, "%b %d %Y").strftime("%Y-%m-%d")
    #     return param

    # for date in datevalue:

#     regex = '\,'
#     param = [re.sub(regex, '', str(i)) for i in param]
#     param = list(map(lambda x:x.strip(), param))
#     param = datetime.strptime([str(item) for item in param], '%b %d %Y')
#     param = [str(i.strip().replace(',', '')) for i in param]
#     param = list(map(str.strip, param))
#     param = [str(x.replace(',', '')) for x in param]
#     param = list(map(lambda x: datetime.strptime(x, "%b %d %Y").strftime('%Y-%m-%d'), param))
#     return param


def clean_poster(param):
    if param:
        try:
            param = param[0]['path']
        except TypeError:
            pass
    return param


def clean_amount_reviews(param):
    param = [item.strip() for item in param]
    param = ''.join(param)
    return param


def clean_approval_percentage(param):
    param = [item.strip().replace('%', '') for item in param]
    param = ''.join(param)
    return param


class CrawlingPipeline(object):
    def process_item(self, item, spider):
        title = clean_title(item['title'])
        critics_consensus = clean_critics_consensus(item['critics_consensus'])
        date = clean_date(item['date'])
        poster = clean_poster(item['images'])
        amount_reviews = clean_amount_reviews(item['amount_reviews'])
        approval_percentage = clean_approval_percentage(
            item['approval_percentage'])

        imdbranking = clean_amount_reviews(item['imdbranking'])

        Movie.objects.create(
            title=title,
            critics_consensus=critics_consensus,
            date=date,
            poster=poster,
            amount_reviews=amount_reviews,
            approval_percentage=approval_percentage,
            imdbranking=imdbranking,
        )

        return item


class CustomImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # for (image_url, image_name) in zip(item['images'], item['title']):
        #     yield scrapy.Request(url=image_url, meta={"image_name": image_name})
        if 'images' in item:
            for image_url, img_name in item['images'].items():
                request = scrapy.Request(url=image_url)
                new_img_name = ('%s.jpg' % (img_name)).replace(" ", "")
                request.meta['img_name'] = new_img_name
                yield request

    def file_path(self, request, response=None, info=None):
        return os.path.join(info.spider.IMAGE_DIR, request.meta['img_name'])


class DeleteNullTitlePipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        if title:
            return item
        else:
            raise DropItem('found null title %s', item)


class DuplicatesTitlePipeline(object):
    def __init__(self):
        self.movie = set()

    def process_item(self, item, spider):
        title = item['title']
        if title in self.movie:
            raise DropItem('duplicates title found %s', item)
        self.movie.add(title)
        return(item)
