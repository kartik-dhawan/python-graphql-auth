from app.auth.types import SignUpEmailInput, SignUpEmailResponse, OtpSignInResponse, PhoneSignInInput, OtpDispatchInput, OtpDispatchResponse, SignInInput, SignInResponse
from app.supabase.config import supabase
from gotrue.errors import AuthApiError
from app.auth.methods import convert_supabase_session_to_tokens


# a function to allow user to sign up using email along with name & password
def user_sign_up(input: SignUpEmailInput) -> SignUpEmailResponse:
    try:
        if not input.email:
            raise Exception("Enter email to continue.")

        # signing up on supabase
        response = supabase.auth.sign_up({
            "email": input.email,
            "password": input.password,
        })

        if not response.user:
            raise Exception(
                "Sign up failed. Please try again. The email might be in use before.")

        # converts session data from supabase to api response
        session_data = convert_supabase_session_to_tokens(response.session)

        return SignUpEmailResponse(id=response.user.id, email=input.email, message="User account created successfully!", session=session_data)
    except AuthApiError as e:
        raise Exception(f"Sign up failed: {str(e.message)}")
    except Exception as e:
        raise Exception(f"Sign up failed: {str(e)}")


# a function solely to dispatch the OTP
def user_phone_otp_dispatch(input: OtpDispatchInput) -> OtpSignInResponse:
    try:
        response = supabase.auth.sign_in_with_otp({
            "phone": input.phone
        })

        return OtpDispatchResponse(message="OTP sent successfully!", phone=input.phone)
    except AuthApiError as e:
        raise Exception(f"Sign up failed: {str(e.message)}")
    except Exception as e:
        raise Exception(f"Verification failed: {str(e)}")


# a function to verify that dispatched OTP with the phone number & then sign the user in/up
def user_phone_otp_verify(input: PhoneSignInInput) -> OtpSignInResponse:
    try:
        response = supabase.auth.verify_otp({
            "phone": input.phone,
            "token": input.otp,
            "type": "sms"
        })

        # converts session data from supabase to api response
        session_data = convert_supabase_session_to_tokens(response.session)

        OtpSignInResponse(id=response.user.id,
                          isValidated=True, session=session_data)
    except AuthApiError as e:
        raise Exception(f"Sign up failed: {str(e.message)}")
    except Exception as e:
        raise Exception(f"OTP Verification failed: ${str(e)}")


def user_email_sign_in(input: SignInInput) -> SignInResponse:
    try:
        response = supabase.auth.sign_in_with_password({
            "email": input.email,
            "password": input.password
        })

        # converts session data from supabase to api response
        session_data = convert_supabase_session_to_tokens(response.session)

        return SignInResponse(id=response.user.id, email=response.user.email, message="Signed in successfully!", session=session_data)
    except AuthApiError as a:
        raise Exception(a.message)
    except Exception as e:
        raise Exception(f"Email sign-in failed: {str(e)}")
