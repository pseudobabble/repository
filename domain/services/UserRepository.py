#!/usr/bin/env python3

from domain.models.User import User
from repository.SqlAlchemyAdaptor import SqlAlchemyAdaptor


class UserRepository(SqlAlchemyAdaptor):

    entity = User

    def get_by_nickname(self, nickname):
        return self.session.query(self.entity).filter_by(nickname=nickname).first()

