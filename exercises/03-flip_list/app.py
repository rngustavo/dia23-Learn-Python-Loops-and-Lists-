arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
largo=len(arr)-1
new_list=[]
for i in range(largo, -1,-1):
    new_list.append(arr[i])
print (f'Initial list: {arr}')
print (f'Final list: {new_list}')
