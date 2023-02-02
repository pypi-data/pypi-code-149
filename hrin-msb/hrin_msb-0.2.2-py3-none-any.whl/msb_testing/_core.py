import django
from django.test.testcases import (TestCase, LiveServerThread, QuietWSGIRequestHandler)
from django.core.servers.basehttp import WSGIServer
from msb_dataclasses import Singleton
from os import environ, path, listdir
from django.conf import settings

DEFAULT_FIXTURES_DIR = "base"
TEST_FIXTURES_DIR = "test"
DECLARED_FIXTURES_DIRS = settings.FIXTURE_DIRS if isinstance(settings.FIXTURE_DIRS, list) else []


class LiveServerThreadWithReuse(LiveServerThread):
	"""
	This miniclass overrides _create_server to allow port reuse. This avoids creating
	"address already in use" errors for tests that have been run subsequently.
	"""

	def _create_server(self):
		return WSGIServer((self.host, self.port), QuietWSGIRequestHandler, allow_reuse_address=True, )


class TestConfig:
	load_default_fixtures: bool = True
	load_test_fixtures: bool = True

	@property
	def default_fixture_dirs(self):
		_fixture_dirs: list = []
		if self.load_default_fixtures:
			_fixture_dirs.append(DEFAULT_FIXTURES_DIR)

			if self.load_test_fixtures:
				_fixture_dirs.append(TEST_FIXTURES_DIR)

			if len(_fixture_dirs) > 0:
				_fixture_config = {path.basename(i): i for i in DECLARED_FIXTURES_DIRS}
				_fixture_dirs = [_fixture_config.get(i) for i in _fixture_dirs if i in _fixture_config.keys()]

		return _fixture_dirs

	def _load_fixtures_in_db(self, *fixtures):
		from django.core import management
		management.call_command('loaddata', *fixtures)

	def __load_default_fixtures(self):
		for fixture_dir in self.default_fixture_dirs:
			_fixture_files = [path.basename(file) for file in sorted(listdir(fixture_dir))]
			self._load_fixtures_in_db(*_fixture_files)

	def __init__(self):
		self.__load_default_fixtures()

	def get(self, key: str = None, default=None):
		return environ.get(f"TEST_{str(key).upper()}", default=default)

	@property
	def auth_credentials(self):
		return dict(user=self.get('AUTH_USER'), password=self.get('AUTH_PASSWORD'), auth_type=self.get('AUTH_TYPE'))
