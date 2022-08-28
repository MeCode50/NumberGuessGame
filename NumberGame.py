import random

top_range = input("Enter a number: ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <=0:
        print('please type a number greater than 0 ')
        quit()

num = random.randrange(101)

