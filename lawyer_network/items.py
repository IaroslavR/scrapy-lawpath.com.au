# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# - Lawyer Name
# - Title/Position
# - Law Firm Name
# - Years Experience
# - Lawyer About/Description
# - Languages Spoken
# - Practice Areas
# - Location/s
# - Join Date
# - Connected to # Clients
# - Source: URL

class LawyerNetworkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	lawyer_name = scrapy.Field()
	title = scrapy.Field()
	firm_name = scrapy.Field()
	years_experience = scrapy.Field()
	lawyer_about = scrapy.Field()
	languages = scrapy.Field()
	practice_areas = scrapy.Field()
	location = scrapy.Field()
	join_date = scrapy.Field()
	connected = scrapy.Field()
	source = scrapy.Field()