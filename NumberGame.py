import random
# let's ask the user to input a number in the top range
top_range = input("Enter a number: ")
# lets check if the the inputed number is a digit or not
if top_range.isdigit():
# if it's a digit, lets convert the digit to an integer
    top_range = int(top_range)
    if top_range <=0:
        print('please type a number greater than 0 ')
        quit()
# if top range isnt a digit
else:
    print("What you entered is not a number, type a number next time")
    quit()

random_num = random.randint(0, top_range)
# variable to tell in what number of guesses he/she got correct
guesses = 0

while True:
    guesses +=1
# lets ask the user to guess a number
    user_guess = input("Guess a number: ")
# lets check if the guessed number is a digit or not
    if user_guess.isdigit():
# if the guessed number is a digit, let convert the digit to an integer
         user_guess = int(user_guess)
# else statment if the huessed number is not a digit
    else:
         print('type in a number next time')
         continue
# if the number guessed is equal to the random number
    if user_guess == random_num:
         print('correct')
         print('you got it in ', guesses, "guesses")
         break
# elif statment to check if the guessed number is below or above the range.
    elif user_guess > random_num:
            print("you are above the range of numbers")
    else:
             print("you are below the range of numbers")

    #print('you got it in ', guesses, "guesses")




