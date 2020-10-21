import unittest
import requests

from bs4 import BeautifulSoup
from GitCraw.repos import Respositories
from GitCraw.types import Type

class TypesTest(unittest.TestCase):

    def testParseOk(self):
        url = 'https://github.com/search?q=Tensorflow&type=Repositories'
        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, "html.parser")
        strategy = Respositories()
        strategyType = Type(strategy)
        response =strategyType.search_params(response.text)
        self.assertEqual(len(response),10)

    def testParseWrong(self):
        url = 'https://github.com/search?q=1231231dsadsa3421&type=Repositories'
        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, "html.parser")
        strategy = Respositories()
        strategyType = Type(strategy)
        response = strategyType.search_params(response.text)
        self.assertEqual(len(response),1)

if __name__ == '__main__':
    unittest.main()
