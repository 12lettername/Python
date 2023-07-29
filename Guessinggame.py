import random

print("Welcome to the guessing game")
print("The computer will choose a number from 1 to 100 \n and you have to guess that number correctly")
val = random.randint(1,100)
def guess(val):
    no_of_guesses = 0
    diff2 = 0
    while True:
        user = int(input("Enter your guess: "))
        diff1 = abs(user - val)
        if diff1 !=0:
            if no_of_guesses ==0:
                if diff1 <=20:
                    print("WARM!")
                    diff2 = abs(user-val)
                    no_of_guesses +=1
                else:
                    print("COLD!")
                    diff2 = abs(user - val)
                    no_of_guesses += 1
            else:
                if diff1 >= diff2:
                    print("COLDER!")
                    diff2 = abs(user - val)
                    no_of_guesses += 1
                elif diff1 <= diff2:
                    print("WARMER!")
                    diff2 = abs(user - val)
                    no_of_guesses += 1
        else:
            print("You have guessed it correclty")
            no_of_guesses += 1
            print(f"No.of guesses: {no_of_guesses}")
            break
guess(val)