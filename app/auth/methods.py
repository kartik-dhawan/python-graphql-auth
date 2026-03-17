from app.auth.types import UmsAuthSession, User
from gotrue.types import Session, User as SupabaseUser


def convert_supabase_session_to_tokens(payload: Session):
    return UmsAuthSession(
        access_token=payload.access_token,
        refresh_token=payload.refresh_token,
        expires_at=payload.expires_at,
        expires_in=payload.expires_in
    )


def manipulate_user_object(payload: SupabaseUser) -> User:
    return User(
        id=payload.id,
        name=payload.user_metadata.get("name") or "",
        email=payload.email,
        createdAt=payload.created_at,
        lastLogin=payload.last_sign_in_at,
        updatedAt=payload.updated_at
    )
