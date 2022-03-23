"""
We create a function that breaks down a quadratic equation someone enters
into a list of a, b, and c values.
"""
from fractions import Fraction as F
from decimal import Decimal as D

def stringClean(x):
    if "x**2" in x:
        x = x.replace("x**2","")

    if "x^2" in x:
        x = x.replace("x^2","")

    if "x" in x:
        x = x.replace("x","")

    for i in range(len(x)):
        if x[i]=="+":
            x = x.replace("+"," ")
    for i in range(len(x)):
            if x[i]=="-":
                x = x.replace("-"," -")

    x=x.split()
    vals=[]

    #print(x)
    for i in range(len(x)):
        vals.append(int(x[i]))


    #If list size only has 2 elements, its because the user probably didnt enter
    #a value for a when inputing the equation (x^2), so we insert a value for 1
    if len(vals) == 2:
            vals.append(vals[1])
            vals[1] = vals[0]
            vals[0] = 1

    return vals
#
"""
Write a function that grabs the factors from each input value
from the quadratic equation
"""
def getFactors(a, c):
    fA = []
    fC = []

    if a > 0:
        for i in range(1,a+1):
            if a%i==0:
                fA.append(i)
                fA.append(a/i)
            if -a%i==0:
                fC.append(-i)
                fC.append(a/-i)

    if a < 0:
        for i in range(a, 0):
            if a%i==0:
                fA.append(i)
                fA.append(a/i)
            if -a%i==0:
                fC.append(-i)
                fC.append(a/-i)

    if c > 0 :
        for i in range(1,c+1):
            if c%i==0:
                fC.append(i)
                fC.append(c/i)
            if -c%i==0:
                fC.append(-i)
                fC.append(c/-i)
    if c < 0:
        for i in range(c,0):
          if c%i==0:
            fC.append(i)
            fC.append(c/i)
          if -c%i==0:
            fC.append(-i)
            fC.append(c/-i)

    return fA, fC
#
"""
Tests to see if the products of the opposing terms add up to term b in
A quadratic equation (i.e. in ax^2+bx+c and (w1+z1)(w2+z2), we want to
find all combinations which w1*z2+z1*w2 == b where w1 and w2 are factors
of a and z1 and z2 are factors of c.
"""
def eq(fA,fC,b,cS):
    for i in range(len(fA)-1):
        for j in range(len(fC)-1):
            if fA[i]*fC[j+1]+fA[i+1]*fC[j] == b:
                if fC[j] < 0:
                    b1 = "-"+str(abs(int(fC[j])))+")"
                else:
                    b1 = "+"+str(int(fC[j]))+")"
                if fC[j+1] < 0 :
                    b2 = "-"+str(abs(int(fC[j+1])))+")"
                else:
                    b2 = "+"+str(int(fC[j+1]))+")"

                if fA[i] == 1:
                    a1 = "(x"
                elif fA[i] == -1:
                     a1 = "(-x"
                else:
                    a1 = "("+str(int(fA[i]))+"x"

                if fA[i+1] == 1:
                    a2 = "(x"
                elif fA[i+1] == -1:
                     a1 = "(-x"
                else:
                    a2 = "("+str(int(fA[i+1]))+"x"

                if a1+b1 == a2+b2:
                    result = a1+b1+"^2"
                else:
                    result = a1+b1+a2+b2

                if cS != 1:
                    cS = str(cS)
                    result = cS+result
                else:
                    result

                xSols = [(-1*fC[j]/fA[i]),(-1*fC[j+1]/fA[i+1])]

                if xSols[0] != int(xSols[0]):
                    xSols[0] = str(int(-1*fC[j]))+"/"+str(int(fA[i]))
                if xSols[1] != int(xSols[1]):
                    xSols[1] = str(int(-1*fC[j+1]))+"/"+str(int(fA[i+1]))

                print(result,"\nx =", xSols[0],",", xSols[1])

def factorer():
    while True:
        x = input("Enter a quadratic equation (-1 to quit):")
        print("\nEq:", x)
        if x == "-1":
            break
        y = stringClean(x)

        a=y[0]; b=y[1]; c=y[2];
        print("a:",a, "b:",b,"c:",c)

        cS = 1
        poly = (b**2)-(4*a*c)
        if(poly < 0 or poly - int(poly)!=0):
            return "The equation is not factorable"

        for i in range(1, 10000):
            if a%i == 0 and b%i == 0 and c%i== 0:
                a=int(a/i);b=int(b/i);c=int(c/i); cS = (int(cS*i))

        pX = (-b+(poly)**.5) / 2*a
        nX = (-b-(poly)**.5) / 2*a

        if pX == nX:
            print("Quadratic Eq Sol:",pX)
        else:
            print("Quadratic Eq Sol:",pX)
            print("Quadratic Eq Sol:",nX)

        eq(getFactors(a,c)[0],getFactors(a,c)[1],b,cS)



factorer()
