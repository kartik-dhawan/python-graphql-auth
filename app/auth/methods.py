from app.auth.types import UmsAuthSession
from gotrue.types import Session


def convert_supabase_session_to_tokens(payload: Session):
    resp = UmsAuthSession(
        access_token=payload.access_token,
        refresh_token=payload.refresh_token,
        expires_at=payload.expires_at,
        expires_in=payload.expires_in
    )
    return resp
