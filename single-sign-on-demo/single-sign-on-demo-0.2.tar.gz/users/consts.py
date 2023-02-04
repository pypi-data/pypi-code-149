import os
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

print(f"GOOGLE_CLIENT_ID {GOOGLE_CLIENT_ID}\n")
print(f"GOOGLE_CLIENT_SECRET {GOOGLE_CLIENT_SECRET}\n")

GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)