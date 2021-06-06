# Program that prints the length of an entered password

username = input('What is your username? ')
password = input('What is your passowrd? ')
hidden_password = '*' * len(password)

print(f'Hey {username}, your password, {hidden_password} is {len(password)} characters long')
