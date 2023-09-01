# Enter your code here. Read input from STDIN. Print output to STDOUT
from fractions import Fraction


A = 500*2
pA = 0.005

defA = ['defA' for _ in range(int(A*(pA)))]

B = 1000*2
pB = 0.008

defB = ['defB' for _ in range(int(B*(pB)))]


C = 2000*2
pC = 0.010

defC = ['defC' for _ in range(int(C*(pC)))]

totalDef = defA + defB + defC

count=0

for pipe in totalDef:
    if pipe=='defA':
        count += 1
        
print(Fraction(count, len(totalDef)))
