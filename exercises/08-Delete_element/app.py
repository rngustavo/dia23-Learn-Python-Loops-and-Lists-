people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
   
    largo=len(people)
    array=[]
    for i in range(largo):
        if  people[i]!=person_name:
            array.append(people[i])

    return array
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))

