# Python program to check if a given year is a leap year or not.

a=int(input('enter: '))
if a%400==0 or a%4==0 and a%100!=0  :
    print('leap year')
else:
    print('not a leap year')

# a=int(input('enter: '))
# if a%4==0 :
#     if a%100==0:
#         if a%400==0:
#             print('leap')
#         else:
#             print('not leap')
#     else:
#         print('leap')
# else:
#     print('not leap')