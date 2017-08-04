# Example frontera project
This is an example frontera project, combining scrapy's quotes example and frontera's `cluster-setup` example.

## How to run it
First off open a bunch (7 should be enough) of terminal windows (tmux is awesome for this).

### First the backend
Run `docker-compose -f docker-compose-backend.yml up -d` to get hbase, kafka, and zookeeper running.

### Next the Storage workers
In a separate terminal window run `python -m frontera.worker.db --config frontier.dbworker --no-incoming`
In another separate terminal window run `python -m frontera.worker.db --no-batches --config frontier.dbworker`

### Next the strategy workers
In a separate terminal windows run `python -m frontera.worker.strategy --config frontier.sworker --partition-id 0`
In another separate terminal window run `python -m frontera.worker.strategy --config frontier.sworker --partition-id 1`

### Next the crawlers
In separate terminal windows run:
- `scrapy crawl quotes -L INFO -s SPIDER_PARTITION_ID=0`
- `scrapy crawl quotes -L INFO -s SPIDER_PARTITION_ID=1`
