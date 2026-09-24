import random

my_num = random.randint(1,20)

guesses = 0
max_guesses = 5

while True:
    try:
        your_num = int(input("Enter a number>>>: "))
        if your_num < 1 or your_num > 20:
            print("Enter a number btn 1 and 20")
            continue
        
        guesses += 1
        
        if your_num == my_num:
            print("SUCCESS!!! ")
            print(f"You have used {guesses} guesses ")
            break
        else:
            print ("TRY AGAIN!!! ")
        print(f"My number is {my_num} yours is {your_num}")
        
        if guesses == max_guesses:
            print ("You are out of guesses")
            print(f"You have used {guesses} guesses ")
            print(f"correct number was {my_num}")
            break
        
    except ValueError:
        print("you must enter a number")