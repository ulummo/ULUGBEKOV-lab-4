import math
p = 1
for n in range(1, 11):
    term = (math.tan(n) / (n**(0.6*n) + n + 1)) * math.factorial(n)
    p*= term

print(p)