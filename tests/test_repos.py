import unittest
import requests

from bs4 import BeautifulSoup
from GitCraw.repos import Respositories


class RepositoriesTest(unittest.TestCase):

    def setUp(self) -> None:
        url = 'https://github.com/search?q=Tensorflow&type=Repositories'
        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, "html.parser")
        self.repositories = Respositories()

    def testRepositoriesParseOk(self):
        self.setUp()
        r = self.repositories.search_gh_data(self.soup)
        self.assertEqual(r[0]["url"],"https://github.com/tensorflow/tensorflow")
        self.assertEqual(len(r),10)

    def testRepositoriesBonus(self):
        self.setUp()
        url = "https://github.com/tensorflow/tensorflow"
        r = self.repositories.get_repo_data(url)
        self.assertEqual(r["extra"]["owner"],"tensorflow")

if __name__ == '__main__':
    unittest.main()
