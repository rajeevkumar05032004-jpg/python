def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd (b,a%b)
    
a = int(input("ENTER A NO : "))
b = int(input("ENTER A NO : "))

print("gcd: ", gcd(a,b))
