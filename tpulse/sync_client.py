"""Sync Client for TCS PULSE api"""
from typing import Dict, Optional

import httpx
from fake_useragent import UserAgent

from tpulse import settings

ua = UserAgent().random


class ClientBase:
    """Base class for API client"""

    def __init__(self, base_url: str):
        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "User-agent": ua,
        }
        data = {"appName": "invest", "origin": "web", "platform": "web"}
        self._client = httpx.Client(base_url=base_url, headers=headers, params=data)

    def __enter__(self) -> "ClientBase":
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        """Close network connections"""
        self._client.close()

    def _get(self, url, data, timeout=settings.TIMEOUT_SEC):
        """GET request to Dadata API"""
        response = self._client.get(url, params=data, timeout=timeout)
        response.raise_for_status()
        return response.json()

    def _post(self, url, data, timeout=settings.TIMEOUT_SEC):
        """POST request to Dadata API"""
        response = self._client.post(url, json=data, timeout=timeout)
        response.raise_for_status()
        return response.json()


class UserClient(ClientBase):
    """User class for tpulse api"""

    BASE_URL = "https://www.tinkoff.ru/api/invest-gw/social/v1/"

    def __init__(self):
        super().__init__(base_url=self.BASE_URL)

    def user_info(self, name: str) -> Optional[Dict]:
        """get user info by username"""
        url = "profile/nickname/%s" % name
        response = self._get(url, data=None)
        return response["payload"] if response["status"] == "Ok" else None

    def user_posts(self, user_id: str, cursor: int, **kwargs) -> Optional[Dict]:
        """get user posts by user id"""
        url = "profile/%s/post" % user_id
        data = {"limit": 30, "cursor": cursor}
        data.update(kwargs)
        response = self._get(url, data)
        return response["payload"] if response["status"] == "Ok" else None


class PostClient(ClientBase):
    """Ticker class for tpulse api"""

    BASE_URL = "https://www.tinkoff.ru/api/invest-gw/social/v1/"

    def __init__(self):
        super().__init__(base_url=self.BASE_URL)

    def posts(self, ticker: str, cursor: int, **kwargs) -> Optional[Dict]:
        """get post info by ticker"""
        url = "post/instrument/%s" % ticker
        data = {"limit": 30, "cursor": cursor}
        data.update(kwargs)
        response = self._get(url, data)
        return response["payload"] if response["status"] == "Ok" else None


class PulseClient:
    """Sync client for tpulse api"""

    def __init__(self):
        self._user = UserClient()
        self._post = PostClient()

    def test(self):
        """test func"""
        pass

    def get_user_info(self, name: str) -> Optional[Dict]:
        """Get user info"""
        return self._user.user_info(name)

    def get_posts_by_user_id(
        self, user_id: str, cursor: int = 999999999, **kwargs
    ) -> Optional[Dict]:
        """Collect last 30 posts for user"""
        return self._user.user_posts(user_id, cursor, **kwargs)

    def get_posts_by_ticker(
        self, ticker: str, cursor: int = 999999999, **kwargs
    ) -> Optional[Dict]:
        """Collect last 30 posts for ticker"""
        return self._post.posts(ticker, cursor, **kwargs)

    def __enter__(self) -> "PulseClient":
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        """Close network connections"""
        self._user.close()
        self._post.close()
