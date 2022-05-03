import random

def main():
    random_number = random.randrange(0,20) 
    print(random_number) 

    print("Guess a number in the range 0-20. You have five tries.") 

    number_of_tries = 0
    guess = False  
    while guess == False and number_of_tries < 5: 
        number_of_tries = number_of_tries + 1
        print()
        try:
            user_input = int(input("Your guess? ")) 
        except ValueError: 
            print("Your guess cannot be converted into an integer") 
        if user_input == random_number: 
            guess = True 
            print("Congratulations! Your guess is correct! It is " + str(random_number) + "!") 
        elif user_input > random_number: 
            print("The number is too high.") 
        elif user_input < random_number: 
            print("The number is too low.") 
    
    if (number_of_tries == 5):
        print()
        print("This is your last try")
        try:
            user_input = int(input("Your guess? ")) 
        except ValueError: 
            print("Your guess cannot be converted into an integer")
        print()


    if (number_of_tries == 5 and guess == False):
        print("Your guesses are incorrect. The right answer is " + str(random_number))
        print("End of program")
        print()

if __name__ == "__main__":
    main()