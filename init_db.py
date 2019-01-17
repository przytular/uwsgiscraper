from sqlalchemy import schema, types
from sqlalchemy.engine import create_engine

metadata = schema.MetaData()

page_table = schema.Table('urls', metadata,
    schema.Column('id', types.Integer, primary_key=True),
    schema.Column('url', types.Unicode(255), default=u''),
)

### CONNECT TO DB
engine = create_engine('mysql+mysqldb://scraper:scraper@127.0.0.1:3306/scraper')
metadata.bind = engine

### CREATE TABLES
metadata.create_all(checkfirst=True)