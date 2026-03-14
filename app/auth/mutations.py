import strawberry
from app.auth.service import user_sign_up
from app.auth.types import SignUpInput, SignUpResponse


@strawberry.type
class AuthMutations:

    @strawberry.mutation
    def signUp(self, input: SignUpInput) -> SignUpResponse:
        return user_sign_up(input)
