# Code for Training on Square Codewars Kata

def square_sum(numbers):
    # your code here
    answer = 0

    for number in numbers:
        answer = answer + (number ** 2)

    print(answer)


square_sum([0, 3, 4, 5])

# The following was the solution posted after my submission
# Uses a for loop inside return statement

# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)