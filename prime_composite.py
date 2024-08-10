number = int(input("Enter anumber : "))
if number <= 1:
    print(f"{number} is neither prime or composite ......")
elif number == 2 or number == 3:
    print(f"{number} is prime number ......")
elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
    print(f"{number} is composite number.........")
else:
    print(f"{number} is prime number.......")