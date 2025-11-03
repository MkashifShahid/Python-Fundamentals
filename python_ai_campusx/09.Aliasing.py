a=4
id_of_a=id(a)
print(id_of_a) #Decimal
B=hex(id(a))
print(B)   #HexaDecimal
b=a  #Called Aliasing kyun k ya same memory address ko Refer kr rha hai.
print(id(b))
print(hex(id(b)))    
#Output
'''
10738480
0xa3db30
10738480
0xa3db30'''


import sys
kk = "Muhammad"
l = kk      # l points to the same string object as k
m = l       # m also points to that same object
print(sys.getrefcount(kk))  # Shows how many references exist(ya same address per refer kry ga jis ke wja sy a refer berh jai ga.)
del kk
del l
del m  #Variables del huwy hin per memory adress sy to nhi .Garbage collecter aisy data ko khod remove kr dy ga .
       #Uss her data ko jis ko koi refer na kr rha ho.
