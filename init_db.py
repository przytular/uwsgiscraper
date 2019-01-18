from sqlalchemy import schema, types
from sqlalchemy.engine import create_engine
from scrapy.utils.project import get_project_settings

config = get_project_settings()
metadata = schema.MetaData()

page_table = schema.Table('urls', metadata,
    schema.Column('id', types.Integer, primary_key=True),
    schema.Column('url', types.Unicode(255), default=u''),
)

### CONNECT TO DB
engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
	config['DB_USER'], config['DB_PASS'], config['DB_HOST'], config['DB_PORT'], config['DB_NAME']))
metadata.bind = engine

### CREATE TABLES
metadata.create_all(checkfirst=True)
