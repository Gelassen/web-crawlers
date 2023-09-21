# web-crawlers
```
$ mk environments
$ cd environments
$ python3-venv dev_env

$ source dev_env/bin/activate

$ cd ~/Workspace/Personal/Project
$ pip3 install tqdm && requests && lxml && pandas
```
## Run over scrapy
```
$ scrapy runspider scraper.py

$ scrapy crawl hh-spider (in case you have implemented a standard scrapy project)

$ scrapy runspider scraper.py -o hh-scraped-results.json (in case you would like to save it into the file)
```
