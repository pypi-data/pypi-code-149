from generallibrary import Log

from generalpackager.api.venv import Venv
from generalfile.test.test_path import PathTest

class TestPyPI(PathTest):
    def test_create_venv(self):
        venv = Venv("new_venv")
        self.assertEqual(False, venv.exists())

        venv.create_venv()
        self.assertEqual(True, venv.exists())

        self.assertEqual(False, venv.active())
        with venv:
            self.assertEqual(True, venv.active())
            self.assertIn(venv.path, venv.list_venv_paths())
        self.assertEqual(False, venv.active())

        venv.upgrade()
        venv.python_version()

    def test_list_python_versions(self):
        Log("root").configure_stream()  # HERE ** Would be nice to configure artifact for github actions
        self.assertGreaterEqual(len(Venv.list_python_versions()), 1)


















