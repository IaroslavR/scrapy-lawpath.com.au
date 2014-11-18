# -*- coding: utf-8 -*-

import scrapy
from lawyer_network.items import LawyerNetworkItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

import re

class LNetworkSpider(CrawlSpider):
	name = "l_network"
	allowed_domains = ["lawpath.com.au"]
	start_urls = (
		'https://lawpath.com.au/lawyer-network',
	)
	rules=(
		Rule(SgmlLinkExtractor(restrict_xpaths = ('//*[@id="paginator"]/div/ul/li/a',)),
			follow=True, callback='parse_item',),
	)
	
	def parse_pass(self, response):
		pass
	
	def additional_data(self, response):
		item = response.meta['item']
		if item['years_experience']: item['years_experience'] = re.findall('\d+', item['years_experience'][0])
		# item['practice_areas'] = response.xpath('').extract() //*[@id="profiles"]/div/div[3]/div[2]
		fields = response.xpath('//*[@id="profiles"]/div/div[3]/div[1]/div/text()').extract()
		for field in fields:
			if 'Joined' in field:
				item['join_date'] = [field.replace('Joined ', '')]
			if 'Connected 'in field:
				item['connected'] = re.findall('\d+', field)
		return item
	
	def parse_item(self, response):
		for node in response.xpath(".//*[@id='lawyer-list']/div[@class='row hidden-phone']"):
			item = LawyerNetworkItem()
			item['lawyer_name'] = node.xpath('div/div/div/div[2]/h3/a/text()').extract()
			item['title'] = node.xpath("div/div/div/div[2]/div[2]/div[1]/div/text()").extract()
			item['firm_name'] = node.xpath("div/div/div/div[2]/div[1]/text()").extract()
			item['years_experience'] = node.xpath("div/div/div/div[2]/h5/div/div/text()").extract()
			item['lawyer_about'] = node.xpath("div/div/div/div[2]/div[3]/text()").extract()
			item['languages'] = node.xpath("div/div/div/div[2]/p[3]/text()").extract()
			item['location'] = node.xpath("div/div/div/div[2]/div[2]/div[2]/div/text()").extract()
			item['source'] = ['https://lawpath.com.au'+node.xpath("div/div/div/div[2]/h3/a/@href").extract()[0]]
			url = item['source'][0]
			request = scrapy.Request(url, callback=self.additional_data)
			request.meta['item'] = item
			yield request
			

# - Practice Areas