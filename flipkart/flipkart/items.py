# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipkartItem(scrapy.Item):
	mobile_name = scrapy.Field()
	mobile_price = scrapy.Field()
	mobile_rating = scrapy.Field()
