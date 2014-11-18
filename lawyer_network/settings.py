# -*- coding: utf-8 -*-

# Scrapy settings for lawyer_network project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lawyer_network'

SPIDER_MODULES = ['lawyer_network.spiders']
NEWSPIDER_MODULE = 'lawyer_network.spiders'
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; rv:33.0) Gecko/20100101 Firefox/33.0"

ITEM_PIPELINES = {'lawyer_network.pipelines.CSVPipeline': 300 }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lawyer_network (+http://www.yourdomain.com)'
