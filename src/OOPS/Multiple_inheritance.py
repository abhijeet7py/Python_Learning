class A:
    varA = "Welcome to class A"
class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

a = C()
print(a.varA)
print(a.varB)
print(a.varC)