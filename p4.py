# AREA OF TRIANGLE USING THREE SIDES
# ABC = √[s × (s – a) × (s – b) × (s – c)].
import math

a=int(input("enter : "))
b=int(input("enter : "))
c=int(input("enter : "))

if (a+b)>c and (b+c)>a and (a+c)>b:
    s = (a + b + c) / 2
    z = s * (s - a) * (s - b) * (s - c)
    # area=math.sqrt(z)
    area = z ** (1 / 2)
    print(area)
else:
    print('sum of two sides should be grater than the third side')
