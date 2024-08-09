data = "sujan"
data11 ="sujan katuwal"
data1 = "KATUWAL"
txt = "Hello, welcome to my world."
x = txt.index("m")
split_txt = txt.split(" ")
print(data.upper())
print(data1.lower())
print(data.capitalize())
print(data11.title())
print(x)
print(split_txt)
print(data.encode())
print(data.swapcase())
print(data.isupper())

data6 = "I love veg food"
print(data6.replace('veg','non-veg'))

# spliting text
email = "sujankatuwal@gmail.com"
split_email_1st= email.split('@')
split_email_2nd = split_email_1st[1]
final_split = split_email_2nd.split('.')
print(split_email_1st)
print(split_email_2nd)
print(final_split)

# alternative
my_email = "Sujan@gmail.com"
split_email = my_email.replace('@','.').split('.')
print(split_email)
right_split = my_email.rsplit('.')
print(right_split)
