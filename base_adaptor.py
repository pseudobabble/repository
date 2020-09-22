#!/usr/bin/env python

class BaseAdaptor(object):
    """
    Interface for entity storage services
    """

    entity = NotImplementedError

    def get_by_id(self, entity_id):
        """
        Get entity by id
        """
        raise NotImplementedError

    def get_by_id_or_fail(self, entity_id):
        """
        Get entity by id or raise EntityNotFoundException
        """
        raise NotImplementedError

    def save(self, entity):
        """
        Persist entity to storage
        """
        raise NotImplementedError
