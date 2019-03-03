cart = {
    'apples': 2,
    'oranges': 3
}

basket = {
    'beer': 90,
    **cart
}

print(basket)
