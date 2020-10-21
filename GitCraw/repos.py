import json
import requests

from bs4 import BeautifulSoup
from GitCraw.strategy import Strategy


class Respositories(Strategy):
    """
    Get GitHub Respositories data
    """

    def get_name(self):
        return('Repositories')

    def get_repo_data(self, url):
        data = {}
        data["url"] = url
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        data["extra"] = {}
        data["extra"]["owner"] = soup.find("a", {"rel": "author"}).text
        data["extra"]["language_stats"] = {}
        languages = soup.findAll(
            "span", {"class": "language-color", "itemprop": "keywords"})
        for language in languages:
            l = language.get("aria-label").split(" ")
            data["extra"]["language_stats"][l[0]] = l[1]
        return data

    def search_gh_data(self, soup):
        repos = []
        respositories = soup.findAll('a', {'class': 'v-align-middle'})
        for link in respositories:
            hydro = link.attrs['data-hydro-click']
            hydro = json.loads(hydro)
            url = hydro['payload']['result']['url']
            repo_data = self.get_repo_data(url)
            repos.append(repo_data)
        return repos
