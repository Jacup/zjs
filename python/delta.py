'''
a * x**2 + b * x + c = 0
'''
from math import sqrt
a = 1
b = 1
c = 0
d = b * b - 4 * a * c

wynik = (('Duzo' if (c == 0) else 'Brak')
if (b == 0)
        else 'x = %f' % (-c)/(b*1.0)
    )if (a == 0) \
    else ('x1 = %f, x2 = %f' % ((-b - sqrt(d))/(2*a), (-b + sqrt(d))/(2*a))) \
    if (d > 0) else \
    ('x = %f' % ((-b)/(2.0*a)) if (d == 0) else "....")
print wynik
