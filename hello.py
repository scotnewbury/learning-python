i = 0
new_name = ''
another_name = ''

name = input('What is your name? ')
print('Hello ' + name + '. Welcome to the Matrix!\n\n')

# test formatted string
print(f'Hey {name}, welcome to the jungle!\n\n')

# looping through string
# also reversed the order
while len(name) > i:
    new_name = name[i] + new_name
    i += 1

another_name = name[::-1]  # quicker way to reverse a string

print(f'This is the new name: {new_name}\n\n')
print(f'This is another new name: {another_name}\n\n')
