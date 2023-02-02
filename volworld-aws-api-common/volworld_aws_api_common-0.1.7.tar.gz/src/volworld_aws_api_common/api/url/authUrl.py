from typing import Final

from volsite_postgres_common.api.CA import CA

from volworld_aws_api_common.test.aws.url import build_api_root_url, build_url

ROOT__: Final[str] = build_api_root_url(CA.Auth)

doSignupUrl: Final[str] = build_url(ROOT__, CA.Signup)

doLoginUrl: Final[str] = build_url(ROOT__, CA.Login)

# doLogoutUrl: Final[str] = build_url(ROOT__, CA.Logout)

currentUserUrl: Final[str] = build_url(ROOT__, CA.UserId)
