# uwsgiscraper
Scrapy with uWSGI service

### Installation
```sh
    $ sudo apt install git docker virtualenv gcc python-dev python3-dev build-essential libmysqlclient-dev
    $ git clone https://github.com/przytular/uwsgiscraper.git
    $ cd uwsgiscraper/
    $ virtualenv env3 -p python3
    $ source env3/bin/activate
    $ pip install -r requirements.txt
```

### Create tables
```sh
	$ python3 init_db.py
```

### Start service
```sh
    $ uwsgi --http 0.0.0.0:9000 --wsgi-file uwsgi/handler.py --touch-reload=uwsgi/uwsgi.touch
```

### Restart service
```sh
    $ touch uwsgi/uwsgi.touch
```
