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
