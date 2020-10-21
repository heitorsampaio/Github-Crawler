#! /usr/bin/env python3

import sys
import json

from GitCraw.gh_types import GHTypes
from GitCraw.types import Type
from GitCraw.gh_connector import GitHubConnectos
from GitCraw.verify import Verify


class Crawler:

    def __init__(self, github):
        self.github = github

    def usage(self):
        return ('To use this crawler run: python3 Scrapper.py <json file>')

    def search_data(self, gh_type, keywords):
        try:
            gh_types = GHTypes.factory_method(gh_type)
            type = Type(gh_types)
            return type.search_params(self.github.get_content(keywords, gh_type))
        except Exception as e:
            print(str(e))
            self.usage()


if __name__ == '__main__':
    crawler = Crawler(GitHubConnectos())
    if len(sys.argv) == 2:
        verify = Verify()
        json_file = sys.argv[1]
        with open(json_file, 'r') as f:
            input_file = json.loads(f.read())
        keywords = ', '.join(input_file['keywords'])
        proxies = input_file['proxies']
        gh_type = input_file['type']
        if verify.verify_params(keywords, gh_type):
            print(crawler.search_data(gh_type, keywords))

    else:
        print(crawler.usage())
