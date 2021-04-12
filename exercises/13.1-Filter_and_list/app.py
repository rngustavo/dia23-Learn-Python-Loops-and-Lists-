
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def isR(value):
    return value[0]=='R'

resulting_names=list(filter(isR, all_names))
print(resulting_names)




