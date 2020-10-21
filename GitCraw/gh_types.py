import logging

from abc import ABC, abstractmethod
from GitCraw.issues import Issues
from GitCraw.repos import Respositories
from GitCraw.wikis import Wikis


class GHTypes(ABC):
    """
    GitHub types to select
    """

    factory = {}
    factory["Repositories"] = Respositories()
    factory["Issues"] = Issues()
    factory["Wikis"] = Wikis()

    @classmethod
    def factory_method(self, gh_types):
        if gh_types in GHTypes.factory.keys():
            return GHTypes.factory[gh_types]
        else:
            return None
