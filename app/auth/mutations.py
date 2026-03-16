import strawberry
from app.auth.service import user_sign_up, user_phone_otp_verify, user_phone_otp_dispatch
from app.auth.types import SignUpEmailInput, SignUpEmailResponse, OtpSignInResponse, PhoneSignInInput, OtpDispatchResponse, OtpDispatchInput


@strawberry.type
class AuthMutations:

    # sign up with email & password only
    @strawberry.mutation
    def signUpWithEmail(self, input: SignUpEmailInput) -> SignUpEmailResponse:
        return user_sign_up(input)

    # sending an actual otp
    @strawberry.mutation
    def authSendOTP(self, input: OtpDispatchInput) -> OtpDispatchResponse:
        # TIP: - next time take phone & otp in same API, otp being optional - if otp is not there, call user_phone_otp_dispatch function - if otp is there, call user_phone_otp_verify function
        return user_phone_otp_dispatch(input)

    # sign up/in with phone & otp only
    @strawberry.mutation
    def signInWithPhone(self, input: PhoneSignInInput) -> OtpSignInResponse:
        # TIP: - this could be merged with dispatch otp mutation & be made just one mutation
        return user_phone_otp_verify(input)
