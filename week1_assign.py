import math
def areaofpolygon(a,n):            #a = length of side of regular polygon, n= number of sides of polygon
    Area = 0
    if n == 3:
        Area = math.sqrt(3)*a*a/2
    elif n == 4:
        Area = a*a
    else:
        print('only three sides and four sided polygon are allowed')
    return Area

side = float(input('lenght of side of polygon:'))
side = abs(side)               # though this is not required as area of both polygons have square term,it was kept for satisfaction
n = int(input('number of sides of polygon:'))
print('Area of',n,' sides polygon is:',format(areaofpolygon(side,n),'.2f'))         # format is used here to roundoff the answer