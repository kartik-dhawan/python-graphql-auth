# TODO: DUMMY PRACTICE CODE FOR NOW

import strawberry
from typing import List


@strawberry.type
class User:
    id: str
    name: str


def getUsersFn():
    return [User(**row) for row in dummyUsers]


def getUserByIdFn(root, id: str) -> User | None:
    foundUser = [User(**row) for row in dummyUsers if row["id"] == id]
    return foundUser[0] if len(foundUser) > 0 else None


dummyUsers = [{"id": "1", "name": "Kartik"}, {"id": "2", "name": "KK"}]


@strawberry.type
class AuthQueries:
    getUsers: List[User] = strawberry.field(resolver=getUsersFn)
    getUserById: User | None = strawberry.field(resolver=getUserByIdFn)
