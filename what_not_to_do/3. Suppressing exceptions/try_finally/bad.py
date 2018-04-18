from resource import Box


def remove_items(box, items_to_remove):
    protected_items = ['socks']
    removed_items = []
    try:  # function for removing items contains open/close functionality!
        box.open()
        for item in items_to_remove:
            if item not in protected_items:
                box.remove(item)
                removed_items.append(item)
    finally:
        box.close()
        return removed_items  # returns before exception is raised!


my_box = Box()
my_box.open()
my_box.put('hat')
my_box.put('shoe')
my_box.close()

my_items = remove_items(my_box, ['hat', 'shorts'])  # exception is ignored!
print(my_items)
