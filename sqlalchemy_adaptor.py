#!/usr/bin/env python

from .base_adaptor import BaseAdaptor

from .exception.entity_not_found import EntityNotFoundException
from .exception.unexpected_entity import UnexpectedEntityException

from . import get_session


class SqlAlchemyAdaptor(BaseAdaptor):
    """
    Persist entities using SQLAlchemy.

    Subclass this class, define an entity on the subclass, using the
    declarative_base provided in the module interface, and add your own methods
    for retrieval or specialised persistence.
    """

    entity = NotImplementedError

    def __init__(self):
        """
        Initialise the adaptor with a session
        """
        self.session = get_session()

    def get_by_id(self, entity_id):
        """
        Get the entity by id

        :param entity_id: int|str
        :return: entity
        """
        return self.session.query(self.entity).get(entity_id)

    def get_by_id_or_fail(self, entity_id):
        """
        Get the entity by id or throw exception

        :param entity_id: int|str
        :return: entity
        """
        entity = self.get_by_id(entity_id)
        if not entity:
            raise EntityNotFoundException(
                '{} with id {} was not found.'.format(
                    self.entity.__name__,
                    entity_id
                )
            )

        return entity

    def save(self, entity):
        """
        Add the entity to the session, and commit. This follows the Aggregate
        pattern.

        :param entity: entity
        """
        if not isinstance(entity, self.entity):
            raise UnexpectedEntityException(
                '{} is not a {}'.format(
                    entity.__class__.__name__,
                    self.entity.__name__
                )
            )

        self.session.add(entity)
        self.session.commit()
