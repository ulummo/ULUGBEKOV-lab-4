import math
s = 0
for n in range(1, 50):
    s=s+(1/2*n**n + 1) * math.sin(math.pi/n)
print(s)