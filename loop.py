# num = 1
# while num <= 100:
#     print(num)
#     num = num + 1



# num = 1
# while num<=50:
#     print(num)
#     if num%2 == 0:
#         print(num," is even.............")
#     else:
#         print(num,"is odd....... ")
#         num = num + 1

data = "This is for loop"
for i in data:
    print("letter", i)  # prints individual characters of the string

    print("......................................................")

    data1 = "123456"
    sum = 0
    for i in data1:
    
     sum = sum + int(i)
     my_sum = int(sum)
    print("The sum of the numbers is: ", my_sum)  

    print("............................")
    data2 = "822457313496"
    highest = 0
    for i in data2:
       if int(i) > highest:
          highest = int(i)
    print("The highest number is: ", highest)


print(".......................................")

# WAP to find lowest number amongs data = "822457313496"
data3 = "822457313496"
lowest = 9
for i in data3:
      if int(i) < lowest:
        lowest = int(i)
print("The lowest number is: ", lowest)


        

