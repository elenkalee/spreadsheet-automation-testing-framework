from urllib.parse import urljoin

import requests


class APIClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/") + "/"
        self.session = requests.Session()

    def request(self, method: str, path: str = "", **kwargs: object) -> requests.Response:
        url = urljoin(self.base_url, path.lstrip("/"))
        return self.session.request(method=method, url=url, **kwargs)

    def get(self, path: str = "", **kwargs: object) -> requests.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str = "", **kwargs: object) -> requests.Response:
        return self.request("POST", path, **kwargs)
