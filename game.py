import random
random_number = random.randrange(1 , 100)
a = 1
while a <= 15:
    guess_number = int(input("Enter any number to match random number : "))
    if guess_number == random_number:
        print("Congratulation you guess right number...")
        break
    elif guess_number < random_number:
        print("Your guess is smaller  than random number....")
    elif guess_number > random_number:
        print("You guess is greater than the random number...")
        a = a + 1
        if a > 15:
         print("Sorry, you've used all your attempts. The correct number was:", random_number)