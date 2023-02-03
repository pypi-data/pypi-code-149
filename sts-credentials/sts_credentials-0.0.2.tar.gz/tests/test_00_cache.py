import unittest


class CredentialsTestCase(unittest.TestCase):
    def test_05_cache(self):
        import time
        from sts_credentials.utils.decorators import ttl_lru_cache

        ttl = 1

        @ttl_lru_cache(ttl=ttl)
        def test_func(i=0):
            return time.time() - i

        f1 = test_func()
        print("get f1 done, waiting")
        time.sleep(ttl / 2)
        f2 = test_func()
        print("get f2 done, waiting")
        time.sleep(ttl * 1.2)
        f3 = test_func()
        print("get f3 done")

        print("cache not timeout")
        self.assertEqual(f1, f2)
        print("cache timeout")
        self.assertNotEqual(f2, f3)
        print("args diff")
        self.assertNotEqual(test_func(111), test_func(222))
        print("args same")
        self.assertEqual(test_func(42), test_func(42))
