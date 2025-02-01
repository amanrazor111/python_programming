# F = (c * 9/5)+32

def faren(x):
    f = (x*9/5)+32
    return(f)

x =  float(input("Enter your temp in celcius: "))

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example
celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")