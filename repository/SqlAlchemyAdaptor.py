#!/usr/bin/env python3
from sqlalchemy.orm import Session

from repository.BaseAdaptor import BaseAdaptor
from repository.EntityNotFoundException import EntityNotFoundException
from repository.UnexpectedEntityException import UnexpectedEntityException

from . import get_session


class SqlAlchemyAdaptor(BaseAdaptor):

    entity = NotImplemented

    def __init__(self):
        self.session = get_session()

    def get_by_id(self, entity_id):
        return self.session.query(self.entity).get(entity_id)

    def get_by_id_or_fail(self, entity_id):
        entity = self.get_by_id(entity_id)
        if not entity:
            raise EntityNotFoundException('{} with id {} was not found.'.format(self.entity.__name__, entity_id))

        return entity

    def save(self, entity):
        if not isinstance(entity, self.entity):
            raise UnexpectedEntityException('{} is not a {}'.format(entity.__class__.__name__, self.entity.__name__))

        self.session.add(entity)
        self.session.commit()
