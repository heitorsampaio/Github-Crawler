import unittest
import requests
from bs4 import BeautifulSoup
from GitCraw.issues import Issues


class IssuesTest(unittest.TestCase):
    def testIssuesParseOk(self):
        url = 'https://github.com/search?q=Tensorflow&type=Issues'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        issues = Issues()
        i = issues.search_gh_data(soup)
        self.assertEqual(
            i[0]["url"], 'https://github.com/tensorflow/community/issues/290')
        self.assertEqual(len(i), 10)


if __name__ == '__main__':
    unittest.main()
