#Assume a function f(x) = x**2 - 3
def f(x):
    f = x**2 - 3
    return f


#Pick two values for a and b
# a = 1
# b = 2
# if(f(a) * f(b)) >= 0: 
#     a += 1
#     b += 1


#Create a function to implement the bisection method algorithm
def getApproximateValue(a, b):
        #Set a confidence level
        cl = 0.005
        t = (a + b) / 2
        c = f(a)
        d = f(b)
        p = f(t)
        
        r = b - a
        while r > cl:
            if p < 0:
                a = t
                c = p
            else:
                b = t
                d = p
            r = b - a
            t = (a + b) / 2
            p = f(t)
        return t

v = getApproximateValue(1, 2)
print(v)

    

