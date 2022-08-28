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

random_num = random.randint(0, top_range)
guesses = 0
while True:
    guesses +=1

    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
         user_guess = int(user_guess)
    else:
         print('type in a number next time')
         continue
    if user_guess == random_num:
         print('correct')
         print('you got it in ', guesses, "guesses")
         break
    else:
        if user_guess > random_num:
            print("you are above the range of numbers")
        else:
             print("you are below the range of numbers")

    #print('you got it in ', guesses, "guesses")




