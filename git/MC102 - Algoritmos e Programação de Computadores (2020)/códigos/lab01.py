from decimal import Decimal
num = Decimal(input())
n1 = num//Decimal('10')
n2 = num%Decimal('10')//Decimal('1')
n3 = num%Decimal('1')//Decimal('0.1')
n4 = num%Decimal('0.1')//Decimal('0.01')
s1 = str(n1)
s2 = str(n2)
s3 = str(n3)
s4 = str(n4)

print('R$',s4+s3+'.'+s2+s1)
