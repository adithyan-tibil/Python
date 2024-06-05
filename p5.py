# Python program to swap two numbers without using a temporary variable.

a=int(input("enter: "))
b=int(input("enter: "))

# a=a+b
# b=a-b
# a=a-b
a,b=b,a
print(a)
print(b)