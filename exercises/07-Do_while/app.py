
#Your code go here:
numero=20
while numero>0:
    if numero %5==0:
        print(f'{numero}!')
    else:
        print(numero)
    numero-=1
    if numero==0:
        print('LIFTOFF')


