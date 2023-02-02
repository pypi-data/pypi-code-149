
from generallibrary import EnvVar

GH_TOKEN = EnvVar("GH_TOKEN", "secrets.PACKAGER_GITHUB_API")
TWINE_USERNAME = EnvVar("TWINE_USERNAME", "secrets.TWINE_USERNAME")
TWINE_PASSWORD = EnvVar("TWINE_PASSWORD", "secrets.TWINE_PASSWORD")

