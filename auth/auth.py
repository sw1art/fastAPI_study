from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy
from config import SECRET_KEY_JWT

cookie_transport = CookieTransport(cookie_name='trades', cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY_JWT, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
