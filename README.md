# Repository
A Python implementation of the DDD Repository pattern. An SQLAlchemy adaptor is provided.

## Usage
Define models using the `declarative_base` provided in the module:
```
#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String

import repository


class User(repository.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)

    def greet(self):
        return 'Hello, I am {}'.format(self.name)
```

Create a repository for that model by subclassing the SQLAlchemy Adaptor:
```
#!/usr/bin/env python3

from domain.models.User import User
from repository.SqlAlchemyAdaptor import SqlAlchemyAdaptor


class UserRepository(SqlAlchemyAdaptor):

    entity = User

    def get_by_nickname(self, nickname):
        return self.session.query(self.entity).filter_by(nickname=nickname).first()

```

Use the model and repository in your application:
```
#!/usr/bin/env python3

import repository

from domain.models.User import User
from domain.services.UserRepository import UserRepository

repository.create_all()

user_repository = UserRepository()

user = User(name='Pseudo', fullname='Pseudo Nym', nickname='Nym')
user_repository.save(user)
user_again = user_repository.get_by_nickname('Nym')

different_user = User(name='An', fullname='An Other User', nickname='Number 2')
user_repository.save(different_user)
different_user_again = user_repository.get_by_nickname('Number 2')


print(user)
print(user_again)
print(user.greet(), ', ', different_user.greet())

print(different_user)
print(different_user_again)
print(user_again.greet(), ', ', different_user_again.greet())
```
