import requests


def scrape(rpc, transaction_hash):
    payload = {
        'jsonrpc': '2.0',
        'method': 'eth_getTransactionByHash',
        'id': 1,
        'params': [transaction_hash],
    }

    headers = {'Content-Type': 'application/json'}

    resp = requests.post(rpc, json=payload, headers=headers)
    transaction_obj = resp.json()

    if 'error' in transaction_obj or transaction_obj['result'] is None:
        return False
    return True

