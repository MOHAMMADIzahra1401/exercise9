import math
def moadele2():

    a=int(input("Enter a for moadele daraje 2:"))
    b=int(input("Enter b for moadele daraje 2:"))
    c=int(input("Enter c for moadele daraje 2:"))
    #ax^2+bx+c
    if a ==0:
        print("pleas Enter iek new number biger than 0 for(a)!")
    else:
        delta=(b**2)-(4*(a*c))
        print(delta)
        if delta>0:
            result1=(-b+math.sqrt(delta))/(2*a)
            result2=(-b-math.sqrt(delta))/(2*a)
            print(result1)
            print(result2)
        elif delta==0:
            result3=(-1*b)/(2*a)
            print(result3)
        elif delta<0:
            print("in moadele daraje 2 hal nemishvad")
moadele2()
