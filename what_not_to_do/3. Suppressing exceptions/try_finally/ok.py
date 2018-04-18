from resource import Box


def remove_items(box, items_to_remove):
    protected_items = ['socks']
    removed_items = []
    for item in items_to_remove:
        if item not in protected_items:
            box.remove(item)
            removed_items.append(item)
    return removed_items


if __name__ == '__main__':
    my_box = Box()

    try:
        my_box.open()
        my_box.put('hat')
        my_box.put('shoe')
        my_items = remove_items(my_box, ['hat', 'shorts'])  # exception is raised correctly
        print(my_items)
    finally:
        my_box.close()
