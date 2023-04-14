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
        print(f'Failure: {transaction_obj}')
        return False

    print(f'Success: {transaction_obj}')
    return True


def verify_bsc_transaction_from_different_rpcs(transaction_hash):
    rpcs = [
        'https://rpc.ankr.com/bsc',
        'https://bsc.rpc.blxrbdn.com',
        'https://bsc.blockpi.network/v1/rpc/public',
        'https://bsc-mainnet.nodereal.io/v1/64a9df0874fb4a93b9d0a3849de012d3',
    ]

    results = []

    for rpc in rpcs:
        result = scrape(rpc, transaction_hash)
        results.append(result)

    successful_requests = len([result for result in results if result])
    if successful_requests >= 3:
        return True
    return False


if __name__ == '__main__':
    verified = verify_bsc_transaction_from_different_rpcs(
        '0xdbd25b2061b2188968144436df0dc5346245482780c6ad2de1f0c078b1507f65'
    )
    print(verified)
