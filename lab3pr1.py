#Sam Traylor, Feb 11.
#purpose of program is to calculate cost-per-square inch of pizzas

import math

pzarea = 0
costper = 0
rad = 0

diameter = float(input('Please enter the diameter of your pizza, in inches:'))
price = float(input('Please enter it''s cost, in dollars:'))

def area(radius):
    pzarea = (radius ** 2) * math.pi
    return pzarea

def cost_per_square_inch(diameter,price):
    rad = diameter / 2
    costper = price / (area(rad))
    costper = round(costper,2)
    return costper

print('The cost is ' + str(cost_per_square_inch(diameter,price)) + ' dollars per sq in')

