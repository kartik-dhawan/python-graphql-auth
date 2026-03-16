import strawberry
from typing import Optional


@strawberry.input
class SignUpEmailInput:
    email: str
    password: str


@strawberry.input
class SignInInput:
    email: str
    # username: str -- later we can use email or username
    password: str


@strawberry.input
class PhoneSignInInput:
    otp: str
    phone: str


@strawberry.input
class OtpDispatchInput:
    phone: str


@strawberry.type
class UmsAuthSession:
    access_token: str
    refresh_token: str
    expires_in: int
    expires_at: int


@strawberry.type
class SignUpEmailResponse:
    email: Optional[str] = None
    id: str
    message: Optional[str] = None
    session: UmsAuthSession


@strawberry.type
class SignInResponse:
    message: Optional[str] = None
    email: str
    id: str
    session: UmsAuthSession


@strawberry.type
class OtpDispatchResponse:
    message: str
    phone: str


@strawberry.type
class OtpSignInResponse:
    message: Optional[str] = None
    isValidated: bool
    id: str
    session: UmsAuthSession
