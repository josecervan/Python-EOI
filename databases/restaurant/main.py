import restaurant as res


# Dispatch table
dispatch = {
    1: res.add_category,
    2: res.add_meal,
    3: res.show_menu,
    4: res.do_nothing
}

# Connection to DB
res.create_db()

print('Welcome to PyFood Restaurant!')
option = res.get_option()

while option != 4:
    dispatch[option]()
    option = res.get_option()

print('Completed execution')
