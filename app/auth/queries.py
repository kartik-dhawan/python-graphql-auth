# TODO: DUMMY PRACTICE CODE FOR NOW

import strawberry
from typing import List
from app.auth.types import UserResponse
from app.supabase.config import supabase_admin
from app.auth.service import get_all_users


@strawberry.type
class AuthQueries:

    @strawberry.field
    def getUsers() -> UserResponse:
        return get_all_users()
