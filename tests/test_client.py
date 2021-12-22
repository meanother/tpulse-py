from unittest import mock

from pytest_httpx import HTTPXMock

from tpulse.sync_client import PostClient, PulseClient, UserClient, ua

client = PulseClient()
args = "?appName=invest&origin=web&platform=web"

headers = {
    "Content-type": "application/json",
    "Accept": "application/json",
    "User-agent": ua,
}


def test_init_user():
    user = UserClient()
    assert user._client.headers["Content-type"] == "application/json"
    assert user._client.headers["Accept"] == "application/json"
    assert user._client.headers["User-agent"] == ua


def test_init_post():
    post = PostClient()
    assert post._client.headers["Content-type"] == "application/json"
    assert post._client.headers["Accept"] == "application/json"
    assert post._client.headers["User-agent"] == ua


def test_get_user_info(httpx_mock: HTTPXMock):
    expected = {
        "id": "08efcec6",
        "type": "personal",
        "nickname": "finvestpaper",
        "status": "open",
        "image": "df91ef92",
        "block": False,
        "description": "description",
        "followersCount": 73,
        "followingCount": 11,
        "isLead": False,
        "serviceTags": [],
        "statistics": {
            "totalAmountRange": {"lower": 1000000, "upper": 3000000},
            "yearRelativeYield": 500.00,
            "monthOperationsCount": 97,
        },
        "subscriptionDomains": None,
        "popularHashtags": [],
        "donationActive": True,
        "isVisible": True,
        "baseTariffCategory": "unauthorized",
        "strategies": [],
    }
    httpx_mock.add_response(
        method="GET",
        headers=headers,
        url=f"{UserClient.BASE_URL}profile/nickname/finvestpaper{args}",
        json={"status": "Ok", "payload": expected},
    )
    actual = client.get_user_info("finvestpaper")
    assert actual == expected


def test_get_posts_by_user_id(httpx_mock: HTTPXMock):
    expected = {
        "nextCursor": 171318,
        "hasNext": False,
        "items": [
            {},
        ],
    }
    httpx_mock.add_response(
        method="GET",
        headers=headers,
        url=f"{UserClient.BASE_URL}post/instrument/AAPL{args}&limit=30&cursor=999999999",
        json={"status": "Ok", "payload": expected},
    )
    actual = client.get_posts_by_ticker("AAPL")
    assert actual == expected


def test_get_posts_by_ticker(httpx_mock: HTTPXMock):
    expected = {
        "nextCursor": 4757390,
        "hasNext": True,
        "items": [],
    }
    httpx_mock.add_response(
        method="GET",
        headers=headers,
        url=f"{UserClient.BASE_URL}profile/08efcec6/post{args}&limit=30&cursor=999999999",
        json={"status": "Ok", "payload": expected},
    )
    actual = client.get_posts_by_user_id("08efcec6")
    assert actual == expected


@mock.patch("tpulse.sync_client.UserClient", autospec=True)
@mock.patch("tpulse.sync_client.PostClient", autospec=True)
def test_context_manager(mock_user, mock_post):
    with PulseClient() as cli:
        cli.test()
    mock_user.return_value.close.assert_called_once()
    mock_post.return_value.close.assert_called_once()
