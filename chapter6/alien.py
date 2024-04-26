# Using a dictionary for the first time.
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'You just earned {new_points} points!')

# How to add key-value pairs.
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with a empty list.

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying calues in a dictionary.

alien_0 = {'color': 'green'}
print(f'The color is {alien_0["color"]}.')

alien_0['color'] = 'yellow'
print(f'The color is now {alien_0["color"]}.')