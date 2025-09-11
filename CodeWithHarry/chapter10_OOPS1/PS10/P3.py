# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?
# Ans ---> No

class Demo:
    a = 14

o = Demo()

print(o.a) # Prints the class attribute as instance attribute is not present

o.a = 123
print(o.a) #Prints the instance attribute as instance attribute is present

print(Demo.a) # Prints the class attribute