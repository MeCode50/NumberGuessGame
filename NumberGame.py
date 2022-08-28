import random

top_range = input("Enter a number: ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <=0:
        print('please type a number greater than 0 ')
        quit()
else:
    print("What you entered is not a number, type a number next time")
    quit()

num = random.randrange(top_range)
print(num)

while True:
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('type in a number next time')
        continue

    

