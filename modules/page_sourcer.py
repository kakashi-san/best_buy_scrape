"""
this module provides implementation for getting page source from url
"""
from abc import ABC, abstractmethod
from pathlib import Path
import requests
from selenium.webdriver import Chrome


class PageSourcer(ABC):
    """
    abstract class to get page source from url
    """
    @property
    def page_url(self):
        """
        getter method for page url
        """
        return self._page_url

    @abstractmethod
    def get_page_source(self):
        """
        abstract method to get page source from the url.
        """

    def __init__(
            self, page_url
    ) -> None:
        self._page_url = page_url


class WebDriverPageSourcer(PageSourcer):
    """
    class to handle page source using webdriver
    """

    def __init__(
            self,
            page_url: str,
            webdriver_path: Path,
    ) -> None:
        super().__init__(page_url)
        self.webdriver_path = webdriver_path


class RequestsPageSourcer(PageSourcer):
    """
    a class to get page source using requests library
    """

    def __init__(
            self,
            page_url: str,
            **kwargs
    ) -> None:
        super().__init__(
            page_url
        )
        self._kwargs = kwargs

    def get_page_source(self):
        return requests.get(
            self.page_url,
            **self._kwargs,
            timeout=5
            ).content


class ChromePageSourcer(WebDriverPageSourcer):
    """
    class to get page source for url using Chrome Driver
    """

    def __init__(
            self,
            page_url,
            webdriver_path
    ) -> None:
        super().__init__(page_url, webdriver_path)

        self.driver = Chrome(
            executable_path=webdriver_path
        )

        self.driver.get(
            url=self.page_url
        )

    def get_page_source(self):
        return self.driver.page_source
