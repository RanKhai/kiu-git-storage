m1 = float(input("мол масса 1"))
m2 = float(input("мол масса 2"))
M1 = float(input("mas1"))
M2 = float(input("mas2"))
v = float(input("объем"))
p = 0
r = 0.082
t = float(input("tempr"))
x = input("c or k")
if x == "c":
    t = t + 273.15
p = (((m1/M1) + (m2/M2))*r*t)/v
print(p,"atm")
