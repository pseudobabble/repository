#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite://')


def get_session():
    sqlite_engine = engine
    Session = sessionmaker(bind=sqlite_engine)
    session = Session()

    return session

Base = declarative_base()


def create_all():
    Base.metadata.create_all(engine)


