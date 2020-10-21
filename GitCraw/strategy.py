from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Abstract method to search gh data
    """

    @abstractmethod
    def search_gh_data(self, soup):
        pass
