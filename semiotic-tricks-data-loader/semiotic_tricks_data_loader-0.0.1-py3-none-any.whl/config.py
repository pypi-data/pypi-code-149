import sys
from logging import INFO, StreamHandler, getLogger

DEFAULT_LOGGER = getLogger(__name__)
DEFAULT_LOGGER.addHandler(StreamHandler(sys.stdout))
DEFAULT_LOGGER.setLevel(INFO)

PATH_TO_GIT_REPOSITORY = "https://github.com/SemioTricks/semiotics_tricks_lfs.git"

NAMES_TO_IGNORE = [".git", "LICENSE", "README.md", ".gitattributes"]
