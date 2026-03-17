# TODO: DUMMY PRACTICE CODE FOR NOW

import strawberry
from typing import List
from app.auth.types import UserResponse, User
from app.supabase.config import supabase_admin
from app.auth.service import get_all_users, get_current_user, get_user_by_id


@strawberry.type
class AuthQueries:

    @strawberry.field
    def getUsers() -> UserResponse:
        return get_all_users()

    @strawberry.field
    def getLoggedInUser() -> User:
        return get_current_user()

    @strawberry.field
    def getUserById(uid: str) -> User:
        return get_user_by_id(uid)
