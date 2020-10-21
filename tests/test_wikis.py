import unittest
import os
import requests

from bs4 import BeautifulSoup
from GitCraw.wikis import Wikis


class WikisTest(unittest.TestCase):
    def testWikisParseOk(self):
        url = 'https://github.com/search?q=Tensorflow&type=Wiki'
        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, "html.parser")
        soup = BeautifulSoup(response.text, "html.parser")
        wikis = Wikis()
        w = wikis.search_gh_data(soup)
        self.assertEqual(w[0]["url"],'https://github.com/tensorflow/tensorflow')
        self.assertEqual(len(w), 10)


if __name__ == '__main__':
    unittest.main()
