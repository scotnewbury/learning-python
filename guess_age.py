import datetime

date = datetime.date.today()
year = date.strftime("%Y")

birth_year = input ('What year were you born? ')
birthday = input ('Have you celebrated your birthday yet? (y/n) ')

if(birthday == 'y'):
  age = int(year) - int(birth_year)
else:
  age = int(year) - int(birth_year) - 1

print(f'Then you must be {age}.')
