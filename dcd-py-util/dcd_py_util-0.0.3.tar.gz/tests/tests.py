import unittest

from dcd_py_util import encryption


class TestEncryption(unittest.TestCase):

    def test_encryption(self):
        plain_text: str = "Plain text to be encrypted."
        encrypted_text: str = encryption.encrypt(plain_text)
        self.assertIsNotNone(encrypted_text)
        decrypted_text: str = encryption.decrypt(encrypted_text)
        self.assertEqual(plain_text, decrypted_text)

    def test_encryption_with_label(self):
        plain_text: str = "Plain text to be encrypted."
        encrypted_text: str = encryption.encrypt_with_label(plain_text)
        self.assertIsNotNone(encrypted_text)
        self.assertTrue(encrypted_text.startswith(encryption.ENCRYPTED_LABEL))
        decrypted_text: str = encryption.decrypt(encrypted_text)
        self.assertEqual(plain_text, decrypted_text)


if __name__ == '__main__':
    unittest.main()
