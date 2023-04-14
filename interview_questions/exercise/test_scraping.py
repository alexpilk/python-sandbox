from unittest.mock import patch

from scraping import scrape


@patch('scraping.requests.post')
def test_posts_as_expected(mock_post):
    rpc = 'https://rpc.ankr.com/bsc'
    tx_hash = '0x123'
    scrape(rpc, tx_hash)
    mock_post.assert_called_once_with(rpc, json={
        'jsonrpc': '2.0',
        'method': 'eth_getTransactionByHash',
        'id': 1,
        'params': [tx_hash],
    }, headers={'Content-Type': 'application/json'})


class FakeResponse:
    def __init__(self, response: dict):
        self.response = response

    def json(self):
        return self.response


def generate_fake_post(response):
    def fake_post(url, *, json, headers):
        return FakeResponse(response)

    return fake_post


@patch('scraping.requests.post', generate_fake_post(response={'error': 'Unexpected error'}))
def test_response_with_error():
    rpc = 'https://rpc.ankr.com/bsc'
    tx_hash = '0x123'
    response = scrape(rpc, tx_hash)
    assert response is False


@patch('scraping.requests.post', generate_fake_post(response={'result': None}))
def test_response_with_empty_result():
    rpc = 'https://rpc.ankr.com/bsc'
    tx_hash = '0x123'
    response = scrape(rpc, tx_hash)
    assert response is False


@patch('scraping.requests.post', generate_fake_post(response={'result': 'ok'}))
def test_response_with_normal_result():
    rpc = 'https://rpc.ankr.com/bsc'
    tx_hash = '0x123'
    response = scrape(rpc, tx_hash)
    assert response is True
