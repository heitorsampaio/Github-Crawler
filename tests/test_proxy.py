import unittest
from GitCraw.proxy import Proxy

class TestProxy (unittest.TestCase):

    def setUp(self):
        self.proxy = Proxy()

    def test_get_proxies_ok(self):
        self.setUp()
        result = self.proxy.get_proxies()
        self.assertGreaterEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()
