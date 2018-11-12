def greet(user_data):
    if 'name' in user_data.keys():
        name = user_data['name']
    else:
        name = 'user'
    print('Hello, {}'.format(name))
