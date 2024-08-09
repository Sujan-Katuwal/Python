
# WAP to take user input email and validate whether it is correct or not
  
email = input("Enter your email : ")
if '@' in email and '.' in email:
    print("Email is valid")
else:
 print("Email is not valid")



#  WAP to take user input mark percentage and find their division

marks = int(input("Enter your marks: "))
if marks >= 80:
   print("Distinction ")
elif marks >= 60 and marks < 80:
   print("First Division")
elif marks >= 50 and marks < 60:
 print("Second Division")
else:
  print(" You are fail")
   