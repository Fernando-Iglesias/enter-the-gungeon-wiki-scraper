"""Utility functions for the wiki scraper."""
import json
import requests

class PageFetcher:
    """Class to fetch pages from the Enter the Gungeon wiki."""
    def __init__(self, file_path: str):
        self.file_path = file_path
        with open(self.file_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)
    def get_full_url(self, path: str) -> str:
        """Get the full URL for a given section."""
        return self.data["base_url"] + path
    def fetch_page(self, url: str):
        """Fetch the content of a page given its URL."""
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(
                f"Failed to fetch data from {url}. "
                f"Status code: {response.status_code}"
            )
        return response.text
    def fetch_page_by_path(self, path: str):
        """Fetch a page by its path."""
        return self.fetch_page(self.get_full_url(path))
    def fetch_guns_page(self):
        """Fetch the guns page content."""
        return self.fetch_page_by_path(self.data["sections"]["guns"])
    def fetch_items_page(self):
        """Fetch the items page content."""
        return self.fetch_page_by_path(self.data["sections"]["items"])
    def fetch_synergies_page(self):
        """Fetch the synergies page content."""
        return self.fetch_page_by_path(self.data["sections"]["synergies"])
    def fetch_enemies_page(self):
        """Fetch the enemies page content."""
        return self.fetch_page_by_path(self.data["sections"]["enemies"])
    def fetch_bosses_page(self):
        """Fetch the bosses page content."""
        return self.fetch_page_by_path(self.data["sections"]["bosses"])
    def fetch_munchers_page(self):
        """Fetch the munchers page content."""
        return self.fetch_page_by_path(self.data["sections"]["munchers"])
