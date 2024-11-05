from abc import ABC, abstractmethod
import requests


class APIClients(ABC):

    @property
    @abstractmethod
    def base_url(self) -> str:
        pass

    def _get(self, url: str, params: dict = {}) -> dict:
        full_url = self.base_url + url

        resource = requests.get(full_url, params=params, timeout=3)
        resource.raise_for_status()
        return resource.json()
