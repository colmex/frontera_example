BOT_NAME = 'quotesbot'

SPIDER_MODULES = ['general.spiders']
NEWSPIDER_MODULE = 'general.spiders'

# Frontera Settings
FRONTERA_SETTINGS = 'frontier.spider'
SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'

SPIDER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 999,
    'frontera.contrib.scrapy.middlewares.seeds.file.FileSeedLoader': 1,
}
DOWNLOADER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 999,
}
