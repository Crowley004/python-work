# Make a series of conditional test.
# Describe each test and predict each test.
# Five must be true and five false.
cars = ['f-150','blazer','mustang','malibu','bronco']
motorcycles = ['fat boy', 'road glide', 'street glide', 'freewheeler', 'low rider']

print('Is car == f-150, I predict True.')
if 'f-150' in motorcycles:
    print("True")
else:
    print('False')

print('\nIs car == blazer, I predict True.')
if 'blazer' in cars:
    print("True")

print('\nIs fat boy == motorcycles, I predict True.')
if 'fat boy' in motorcycles:
    print("True")

print('\nIs low rider == motorcycles, I predict True.')
if 'low rider' in motorcycles:
    print(True)

print('\nIs malibu == cars, I predict True.')
if 'malibu' in cars:
    print("True")

meat = 'chicken'
print('\nIs tofu == to meat, I predict False.')
print(meat == 'tofu')

print('\nIs chik\'n == to meat, I predict False.')
print(meat == 'chick\'n')

print('\nIs Chick peas == meat, I predict False.')
print('chick peas' == meat)

print('\nIs byond burger == meat, I perdict False.')
print('byond burger' == meat)

