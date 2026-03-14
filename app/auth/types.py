import strawberry
from typing import Optional


@strawberry.input
class SignUpInput:
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    password: str


@strawberry.type
class SignUpResponse:
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    id: str
