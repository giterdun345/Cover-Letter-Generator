# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 23:08:58 2019

@author: KETT
"""

import scrapy


class jobhero(scrapy.Spider):
    name = "jobhero"
    start_urls = ["https://www.jobhero.com/sample-cover-letters/"]
   
    def parse(self, response):
        # xpath_title = "//h2[@class='post-title']/a/text()"
        xpath_link = "//h2[@class='post-title']/a/@href"
      
        for url in response.xpath(xpath_link):
            yield response.follow(url, self.parse_raw_letter)
            
        
    def parse_raw_letter(self, response):
        
        yield {
               'raw': response.xpath("//div[@style='border: 2px solid black; padding: 25px; margin: 5px;']/p/text()").getall(), 
               'raw_title' : response.xpath("//h1/text()").get()
              }