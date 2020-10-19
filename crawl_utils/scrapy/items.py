import scrapy


class GeneralNewsItem(scrapy.Item):
    data_source = scrapy.Field()
    domain = scrapy.Field()
    domain_1 = scrapy.Field()
    domain_2 = scrapy.Field()
    domain_3 = scrapy.Field()
    title = scrapy.Field()
    content_url = scrapy.Field()
    content_source = scrapy.Field()
    author = scrapy.Field()
    pub_time = scrapy.Field()
    content = scrapy.Field()
    html = scrapy.Field()
    labels = scrapy.Field()
    content_uuid = scrapy.Field()
    create_time = scrapy.Field()
    zc_index = scrapy.Field()
    zc_theme = scrapy.Field()
    zc_finish_date = scrapy.Field()
    zc_pub_font = scrapy.Field()
    sub_file_list = scrapy.Field()
    effectiveness = scrapy.Field()
    abolition_date = scrapy.Field()
    zcwj = scrapy.Field()