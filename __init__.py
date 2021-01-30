#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.sqlite')


def get_session():
    """
    Get a session for persistence and retrieval.

    :return: Session
    """
    sqlite_engine = engine
    session_factory = sessionmaker(bind=sqlite_engine)
    Session = scoped_session(session_factory)
    session = Session()

    return session


Base = declarative_base()


def create_all():
    """
    Create database tables.
    """
    Base.metadata.create_all(engine)
