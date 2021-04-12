Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
# the magic go here:
    F = (x * 1.8) + 32
    return F
result = list(map(fahrenheit_values, Celsius_values))
print(result)

