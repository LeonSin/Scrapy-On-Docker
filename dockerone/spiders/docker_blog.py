# -*- coding: utf-8 -*-
import scrapy


class DockerBlogSpider(scrapy.Spider):
    name = "docker-blog"
    allowed_domains = ["dockerone.com"]
    start_urls = (
        'http://www.dockerone.com/article/',
    )

    def parse(self, response):
    	filename = response.url.split("/")[-2]
    	open(filename, 'wb').write(response.body)