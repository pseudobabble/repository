#!/usr/bin/env python
from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.sqlite')


def get_session():
    """
    Get a session for persistence and retrieval. This can be used as a
    contextmanager to provide transaction wrapping in controllers

    :return: Session
    """
    sqlite_engine = engine
    session_factory = sessionmaker(bind=sqlite_engine)
    Session = scoped_session(session_factory)
    session = Session()

    return session


def transaction(function):
    @wraps(function)
    def get_session_for_transaction(*args, **kwargs):
        session = get_session()
        try:
            function(*args, **kwargs)
            session.flush()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    return get_session_for_transaction


Base = declarative_base()


def create_all():
    """
    Create database tables.
    """
    Base.metadata.create_all(engine)
