# just testing out lists

def print_list(list):
  loop = 0
  list_length = len(list)
  
  print(f'\n\nHere\'s the current list: ')
  while loop < list_length:
    print(f'{list[loop]}')
    loop +=1
  print

simple_list = [
  'apple',
  'banana',
  'cherry',
  'date',
  'eggplant'
]

print_list(simple_list)

simple_list.append(input('\n\nWhat item do you want to add? '))

print_list(simple_list)

# challenge exercise lecture 43
# using this list: 
  # basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
  # access "Oranges" and print it:
  # print(basket[1][1][0])

