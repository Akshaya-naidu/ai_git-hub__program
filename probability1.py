# Enter your code here. Read input from STDIN. Print output to STDOUT

from fractions import Fraction

favourable=0

for die1 in range(1,7):
    for die2 in range(1,7):
        if die1!=die2 and die1+die2 ==6:
            favourable +=1
            
total= 36

prob=Fraction(favourable, total)
print(prob)
