# -*- coding: utf-8 -*-
import scrapy
from ..items import FlipkartItem

class flipkart_Spider(scrapy.Spider):
    name = 'flipkart'
    pageno=2 #next page_no to start scraping after first page is over
    start_urls = ['https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'] #website you want to scrape

    def parse(self, response):
        items = FlipkartItem()
        mobile_name = response.css('._3wU53n::text').extract() #to get the text from css selector
        mobile_price = response.css('._2rQ-NK::text').extract() #to get the text from css selector
        mobile_rating = response.css('.hGSR34::text').extract() #to get the text from css selector
        items['mobile_name'] = mobile_name
        items['mobile_price'] = mobile_price
        items['mobile_rating'] = mobile_rating

        yield items

        if flipkart_Spider.pageno<=5:

            nextpage='https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+ str(flipkart_Spider.pageno)
            flipkart_Spider.pageno+=1
            yield response.follow(nextpage, callback = self.parse)

        
