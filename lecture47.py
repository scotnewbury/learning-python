#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

# friends.append(new_friend[0])

friends.extend(new_friend) # does not require index for solution, better?

print(sorted(friends))
