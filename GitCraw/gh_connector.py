import requests

from itertools import cycle
from GitCraw.proxy import Proxy


class GitHubConnectos(object):
    """
    Module to connect with Github with proxies
    """

    def __init__(self):
        self.url = "https://github.com/search?q={}&type={}"

    def get_content(self, data):
        proxyClass = Proxy()
        proxies = proxyClass.get_proxies()
        proxy_pool = cycle(proxies)
        for i in range(1, 11):
            proxy = next(proxy_pool)
            try:
                url = self.url_format(data)
                response = requests.get(
                    url, proxies={"http://" + proxy: "https://" + proxy})
                if response.status_code == 200:
                    return response.text
                else:
                    return "No reponse of GitHub"
            except Exception as e:
                print(str(e))

    def url_format(self, words):
        keywords = words[1].replace(",", "+")
        return self.url.format(keywords, words[2])
