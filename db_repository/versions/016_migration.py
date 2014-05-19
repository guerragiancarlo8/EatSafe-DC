from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
restaurants = Table('restaurants', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('address', String),
    Column('latitude', Integer),
    Column('longitude', Integer),
    Column('price', Integer),
    Column('tel', String),
    Column('website', String),
    Column('category', Integer),
)

restaurants = Table('restaurants', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('address', String(length=120)),
    Column('tel', String(length=64)),
    Column('price', Integer),
    Column('website', String(length=64)),
    Column('longitude', Integer),
    Column('latitude', Integer),
    Column('risklevelsea', Integer),
    Column('risklevelnut', Integer),
    Column('risklevelday', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['restaurants'].columns['category'].drop()
    post_meta.tables['restaurants'].columns['risklevelday'].create()
    post_meta.tables['restaurants'].columns['risklevelnut'].create()
    post_meta.tables['restaurants'].columns['risklevelsea'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['restaurants'].columns['category'].create()
    post_meta.tables['restaurants'].columns['risklevelday'].drop()
    post_meta.tables['restaurants'].columns['risklevelnut'].drop()
    post_meta.tables['restaurants'].columns['risklevelsea'].drop()
