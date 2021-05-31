i = 0
new_name = ''
name = input('What is your name? ')
print('Hello ' + name + '. Welcome to the Matrix!')

# test formatted string
print(f'Hey {name}, welcome to the jungle!')

# looping through string
# also reversed the orger
while len(name) > i:
    print(name[i])
    new_name = name[i] + new_name
    i += 1

print(f'This is the new name: {new_name}')
