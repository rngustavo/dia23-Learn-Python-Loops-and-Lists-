list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(lista):
    odd=[]
    even=[]
    full=[]
    for number in list_of_numbers:
        if number % 2==0:
            even.append(number)
        else:
            odd.append(number)
    
    full.append(odd)
    full.append(even)
    return full




print(merge_two_list(list_of_numbers))
