theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def iswoko(item):
    if item==1:
        return 'wiki'
    else:
        return 'woko'

lista=list(map(iswoko, theBools))
print (lista)

