# PRIME NUMBER

n=int(input('enter'))
for i in range(2,n):
    if n%i==0:
        print('not a prime number')
        break
if n<2:
    print('not a prime')
else:
    print('Prime')

# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             print('not a prime number')
#             break
#       if n<2:
#           print('not a prime')
#     else:
#         print('Prime')

# prime(int(input('enter')))

