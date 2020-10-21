import unittest
from GitCraw.gh_connector import GitHubConnectos

class TestGitHub(unittest.TestCase):
    def setUp(self):
        self.github=GitHubConnectos()
        self.words = 'tensorflow'
        self.keywords = 'Repositories'

    def test_url_format_ok(self):
        self.setUp()
        result =self.github.url_format(self.words, self.keywords)
        self.assertEqual('https://github.com/search?q=tensorflow&type=Repositories',result)

    def test_get_content_ok(self):
        self.setUp()
        result = self.github.get_content(self.words, self.keywords)
        self.assertIsInstance(result,str)

    def test_get_content_wrong(self):
        self.setUp()
        words = 'dsadsadsawee21'
        keywords = 'Repositories'
        result = self.github.get_content(words, keywords)
        self.assertIsInstance(result,str)

if __name__ == '__main__':
    unittest.main()
