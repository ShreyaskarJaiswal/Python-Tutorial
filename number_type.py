import decimal as D     # imports decimal library as D
import fractions as fr  # imports fraction library as fr
import math as          # imports math library as fr

var1=5
var2=1.9
var3= '6+7j'
var4=complex(var3)      #gives the complex number of var3 
var5=D.Decimal(5.3)     #gives decimal precision upto fermi level
var6=fr.Fraction(3.3)   #gives fractional part of the given number

print(type(var1))       #print the type of the var1
print(type(var2))       #print the type of the var2
print(type(var3))       #print the type of the var3
print(type(var4))       #print the type of the var4
print(var4.real)        #print the real part of the var4
print(var5)             #print var5
print(var6)             #print var6
print(m.pi)             #print the value of pi
print(m.sin(0))         #print the value of sin 0
print(m.exp(5))         #print the value of e^5
print(m.factorial(6))   #print the value of 6!


a=10                    #global
def test():
    b=12                #local 
    print(a)
    print(b)
print(a)
#print(b)



