from decimal import *

def half_rising():

    list_1 = []

    x = Decimal('2')

    while (x) <= 5.5:
        list_1.append(x)
        x+= Decimal('0.5')

    print(list_1)

half_rising()