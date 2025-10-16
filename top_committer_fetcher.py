from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class TopCommitters:
    """Base class for fetching and parsing committers.top pages."""

    def __init__(self) -> None:
        self.base_url: str = "https://committers.top/"

    def fetch_and_parse(self, url: str) -> BeautifulSoup:
        """Fetch URL and parse HTML content."""
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data: {response.status_code}")
        html = BeautifulSoup(response.text, "html.parser")
        return html


class MainPage(TopCommitters):
    """Fetches country list from main page."""

    def __init__(self) -> None:
        super().__init__()
        self.url = self.base_url
        self._countries: dict[str, str] = {}

    def fetch_countries(self) -> None:
        """Parse country names and URLs from main page."""
        html = self.fetch_and_parse(self.url)
        links = html.select(".country-list li a")

        for a in links:
            country_name = a.text.strip()
            href = a.get("href")
            if isinstance(href, str):
                country_url = urljoin(self.base_url, href)
                self._countries[country_name] = country_url
            else:
                raise ValueError("Invalid href in country link")

    @property
    def countries(self) -> dict[str, str]:
        """Get country name to URL mapping."""
        return self._countries


class CountryPage(TopCommitters):
    """Fetches committer rankings for a specific country."""

    def __init__(self, name: str, url: str) -> None:
        super().__init__()
        self.name = name
        self.url = url
        self.public_url: str | None = None
        self.private_url: str | None = None
        self._commit_ranks: dict[str, int] = {}
        self._public_ranks: dict[str, int] = {}
        self._private_ranks: dict[str, int] = {}

    def fetch_committers(self) -> None:
        """Fetch and parse all ranking types (commit, public, private)."""
        self.__process_page(self.url, self._commit_ranks, need_further_url=True)
        if self.public_url:
            self.__process_page(self.public_url, self._public_ranks)
        if self.private_url:
            self.__process_page(self.private_url, self._private_ranks)

    @property
    def ranks(self) -> dict[str, dict[str, int]]:
        """Get all ranking dictionaries by type."""
        return {
            "commit": self._commit_ranks,
            "public": self._public_ranks,
            "private": self._private_ranks,
        }

    def __process_page(
        self, url: str, rank_dict: dict[str, int], need_further_url: bool = False
    ) -> None:
        """Parse user rankings from a page and extract public/private URLs."""
        html = self.fetch_and_parse(url)
        rows = html.select(".user-list tbody tr")

        for row in rows:
            id = row.get("id")
            if not isinstance(id, str):
                raise ValueError("Missing or invalid id attribute in row")
            cols = row.find_all("td")
            if len(cols) < 3:
                raise ValueError("Unexpected table structure")
            rank = cols[2].text.strip()
            rank_dict[id] = int(rank)

        if need_further_url:
            urls = html.select(".mode-selector a")
            for a in urls:
                href = a.get("href")
                if not isinstance(href, str):
                    raise ValueError("Invalid href in mode selector link")
                full_url = urljoin(self.base_url, href)
                if "public" in full_url:
                    self.public_url = full_url
                elif "private" in full_url:
                    self.private_url = full_url
