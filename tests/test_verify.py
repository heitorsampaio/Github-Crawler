import unittest
import json

from GitCraw.verify import Verify

class TestVerify(unittest.TestCase):

    def set_up(self):
        self.verify = Verify()

    def testKeywordsOk(self):
        self.set_up()
        result = self.verify.verified_type("Issues")
        self.assertEqual(True,result)

    def testKeywordsWrong(self):
        self.set_up()
        a = "a".encode("ascii")
        result = self.verify.verified_type(a)
        self.assertEqual(False,result)

    def testVerifyParamsOk(self):
        self.set_up()
        with open('../GitCraw/input.json', 'r') as f:
            input_file = json.loads(f.read())
        keywords = ', '.join(input_file['keywords'])
        gh_type = input_file['type']
        result = self.verify.verify_params(keywords, gh_type)
        self.assertEqual(True,result)

    def testVerifyParamsWrong(self):
        self.set_up()
        with open('../GitCraw/input_wrong.json', 'r') as f:
            input_file = json.loads(f.read())
        keywords = ', '.join(input_file['keywords'])
        gh_type = input_file['type']
        result = self.verify.verify_params(keywords, gh_type)
        self.assertEqual(False,result)

    def testverified_typeOk(self):
        self.set_up()
        result = self.verify.verified_type("Repositories")
        self.assertEqual(True,result)

    def testverified_typeWrong(self):
        self.set_up()
        result = self.verify.verified_type("XX")
        self.assertEqual(False,result)

if __name__ == '__main__':
    unittest.main()
