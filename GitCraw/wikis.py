import json

from strategy import Strategy


class Wikis(Strategy):
    """
    Get GitHub wikis data
    """

    def get_name(self):
        """
        Get gh types
        """

        return 'Wikies'

    def search_gitHub_data(self, soup):
        wikis_url = []
        wikis = soup.findAll("div", {"class": "f4 text-normal"})
        for wiki in wikis:
            a = wiki.contents[1].attrs["data-hydro-click"]
            data_hydro = json.loads(a)
            url = {"url": data_hydro['payload']['result']['url']}
            wikis_url.append(url)
        return wikis_url
