data = [1,3,5,2,3,4,7,10,76,44,-2,-9,5,7,9,-1,0,90,101,-4,-2,-6,8]
print("list befort sorting: ", data)
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] >= data[j]:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
print("list after sorting : ", data)

print("....................................")
print("Sorting a list in descending order")

print("list before sorting : ", data)
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] <= data[j]:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
print("list after sorting in decending oreder :  ", data)