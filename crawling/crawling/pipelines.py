import scrapy, os
from movie.models import Movie
from scrapy.pipelines.images import ImagesPipeline
from datetime import datetime

def clean_title(param):
    return param

def clean_critics_consensus(param):
    return ' '.join(param)

def clean_date(param):
    # param = datetime.strptime([str(item) for item in param], '%b %d %Y')
    param = [str(i.strip().replace(',', '')) for i in param]
    # param = list(map(str.strip, param))
    # param = [str(x.replace(',', '')) for x in param]
    # param = list(map(lambda x: datetime.strptime(x, "%b %d %Y").strftime("%Y %m %d"), param))
    return param

def clean_poster(param):
    if param:
        param = param[0]['path']
    return param

def clean_amount_reviews(param):
    return param.strip()

def clean_approval_percentage(param):
    return param.strip().replace('%', '')


class CrawlingPipeline(object):
    def process_item(self, item, spider):
        title = clean_title(item['title'])
        critics_consensus = clean_critics_consensus(item['critics_consensus'])
        date = clean_date(item['date'])
        poster = clean_poster(item['images'])
        amount_reviews = clean_amount_reviews(item['amount_reviews'])
        approval_percentage = clean_approval_percentage(item['approval_percentage'])

        Movie.objects.create(
            title=title,
            critics_consensus=critics_consensus,
            date=date,
            poster=poster,
            amount_reviews=amount_reviews,
            approval_percentage=approval_percentage,
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