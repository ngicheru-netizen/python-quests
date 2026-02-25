# Ask to put in parameters
print("Hello, please input the following parameters!")

# declare the variables
a = 0
b = 0
# creating the function
def Calculate(a,b):
    a = int(input("lenght: "))
    b = int(input("width: "))
    area = a * b
    print(f"the area is {area}")
    return area

Calculate(a,b)

