requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}')
    print('\n Finished making your pizza.')
else:
    print('Are you sure you want a plain pizza?')