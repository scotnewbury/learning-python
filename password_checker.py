# Program that prints the length of an entered password

username = input('What is your username? ')
password = input('What is your passowrd? ')
password_length = len(password)
hidden_password = '*' * password_length

print(f'Hey {username}, your password, {hidden_password} is {password_length} characters long')
