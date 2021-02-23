import math

def refunc(a,step,n):
    if step == n:
        print("%.2e" % a)
        return
    else:
        step += 1
        b = (1/75)*a**2+math.tan(a)
        a=b
        refunc(a,step,n)

step = 1
a = 8
n = (int (input("n")))
refunc (a,step,n)