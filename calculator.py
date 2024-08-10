first_number = int(input("Enter firstnumber : "))
operator = input("Enter operator :")
second_number = int(input("Second number : "))
if operator == '+':
    print(first_number + second_number, ": u performed addition")
elif operator == '-':
 print(first_number - second_number, ": u perform substraction")
elif operator == '*':
   print(first_number * second_number, ": u performed multiplication")
elif operator == '/':
   print(first_number / second_number, "u perform") 
else:
   print("Invalid operator")