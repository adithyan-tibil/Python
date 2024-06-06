mark = []
tot = 0
print("Enter Marks Obtained in 5 Subjects: ")
for i in range(5):
    mark.insert(i, input())

for i in range(5):
    tot = tot + int(mark[i])
per = (tot*100)/500
print("your total marks is",tot)
print("your percentage is",per)

if per>=91 and per<=100:
    print("Your Grade is A1")
elif per>=81 and per<91:
    print("Your Grade is A2")
elif per>=71 and per<81:
    print("Your Grade is B1")
elif per>=61 and per<71:
    print("Your Grade is B2")
elif per>=51 and per<61:
    print("Your Grade is C1")
elif per>=41 and per<51:
    print("Your Grade is C2")
elif per>=33 and per<41:
    print("Your Grade is D")
elif per>=21 and per<33:
    print("Your Grade is E1")
elif per>=0 and per<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")


    #checking for the pull request
