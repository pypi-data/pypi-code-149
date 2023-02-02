from ._core import (LiveServerThreadWithReuse, TestConfig)
from django.test import LiveServerTestCase


class UnitTestConfig(TestConfig):
	pass


class UnitTest(LiveServerTestCase, UnitTestConfig):
	port = 8000
	server_thread_class = LiveServerThreadWithReuse

	def __init__(self, *args, **kwargs):
		LiveServerTestCase.__init__(self, *args, **kwargs)
		UnitTestConfig.__init__(self)

	def setUp(self) -> None:
		"""
		 implement this
		"""
		pass
