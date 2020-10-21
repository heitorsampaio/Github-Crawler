import requests


from lxml.html import fromstring


class Proxy:
    """
    Get proxy list from https://free-proxy-list.net/
    """

    def get_proxies(self):
        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')
                                  [0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        if len(proxies) == 0:
            print("There was an error setting the proxis because there wasn't a usable one. Here are some static proxys "
                  "to use.")
            return ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080',
                    '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128',
                    '13.92.196.150:8080']
        else:
            return proxies
