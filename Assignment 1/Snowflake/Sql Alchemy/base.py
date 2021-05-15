# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#import snowflake.connector as sf

engine = create_engine("snowflake://username:password@account/sevir")

engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")

Session = sessionmaker(bind=engine)

Base = declarative_base()
