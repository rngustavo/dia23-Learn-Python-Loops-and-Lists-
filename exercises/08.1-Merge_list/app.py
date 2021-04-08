chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    fulllist=[]
    for i in chunk_one:
        fulllist.append(i)
    for i in chunk_two:
        fulllist.append(i)
    return fulllist
           


    
print(merge_list(chunk_one, chunk_two))
