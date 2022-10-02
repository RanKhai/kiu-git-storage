s = []
k = 0
s = input()
s = s.split()
count = len(s)
for i in range(len(s)):
    if s[i] == "sheep":
        count -= 1
    else:
        k = count - 1
        print(" ")
if k == 0:
    print("не ешь наших овец,проваливай!",s)
else:
    print("волк хочет съесть",k)
