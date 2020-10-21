
# Github Crawler 👁‍
Github Crawler challange is part of hiring process of RedPoints. This crawler can scraper the 1st page of gihub search, including Repositories, Issues and Wikis.

> This is a example of output

    {'url': 'https://github.com/tensorflow/tensorflow', 
    'extra': {'owner': 'tensorflow', 'language_stats': {'C++'}}

# Usage 🚀
**Install the requirements**

    sudo pip3 install -r requirements.txt

**Runing the tests**

    python3 -m unittest discover -v

**Runing Production**

    python3 Scrapper.py <json input file>

