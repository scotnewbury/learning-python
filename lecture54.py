#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

user_profile = {
  'age': 20,
  'username': 'Johnny',
  'weapons': ['sword', 'axe', 'bow'],
  'is_active': True,
  'clan': 'Bone Crushers'
}

#2 iterate and print all the keys in the above user.
print(user_profile.keys())

#3 Add a new weapon to your user
# print(user_profile['weapons'])
# user_profile['weapons'] += ['dagger']
# print(user_profile['weapons'])

print(user_profile['weapons'])
user_profile['weapons'].append('dagger')
print(user_profile['weapons'])

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value. 
