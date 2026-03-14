from app.auth.types import SignUpInput, SignUpResponse
from app.supabase.config import supabase
from gotrue.errors import AuthApiError


# a function to allow user to sign up either using phone or email along with name & password
def user_sign_up(input: SignUpInput) -> SignUpResponse:
    try:
        # base payload
        payload = {"name": input.name}

        if not input.email and not input.phone:
            raise Exception(
                "Enter either your phone number or email to continue.")

        # switching to email or phone sign up depending upon user input
        if input.email:
            payload["email"] = input.email
        else:
            payload["phone"] = input.phone

        # signing up on supabase
        response = supabase.auth.sign_up({
            **payload,
            "password": input.password,
            "options": {
                "data": {"name": input.name}
            }
        })

        if not response.user:
            raise Exception(
                "Sign up failed. Please try again. The email/phone might be in use before.")

        return SignUpResponse(id=response.user.id, name=input.name, email=input.email, phone=input.phone)
    except AuthApiError as e:
        raise Exception(f"Sign up failed: {str(e.message)}")
    except Exception as e:
        raise Exception(f"Sign up failed: {str(e)}")
