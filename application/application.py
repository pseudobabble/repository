#!/usr/bin/env python3
import repository

from domain.models.User import User
from domain.services.UserRepository import UserRepository

repository.create_all()


user = User(name='Pseudo', fullname='Pseudo Nym', nickname='Nym')

user_repository = UserRepository()
user_repository.save(user)

user_again = user_repository.get_by_nickname('Nym')

print(user)
print(user_again)

