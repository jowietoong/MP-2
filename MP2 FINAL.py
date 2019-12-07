from math import sqrt
import numpy as np

x1 = int(input('x axis of first point: '))
y1 = int(input('y axis of first point: '))
x2 = int(input('x axis of second point: '))
y2 = int(input('y axis of second point: '))
x3 = int(input('x axis of third point: '))
y3 = int(input('y axis of third point: '))

xy1 = (x1**2) + (y1**2)
xy2 = (x2**2) + (y2**2)
xy3 = (x3**2) + (y3**2)
matrix = np.array([(xy1, x1, y1, 1), (xy2, x2, y2, 1), (xy3, x3, y3, 1)], dtype=float)

xy = matrix[0:,1:]
detxy = np.linalg.det(xy)
rndxy = round(detxy)

a1 = matrix [0:, 0]
a2 = matrix [0:, 2]
a3 = matrix [0:, 3]
x = np.column_stack((a1,a2,a3))
detx = -1 * (np.linalg.det(x))
rndx = round(detx)

b1 = matrix [0:, 0]
b2 = matrix [0:, 1]
b3 = matrix [0:, 3]
y = np.column_stack((b1,b2,b3))
dety = np.linalg.det(y)
rndy = round(dety)

c1 = matrix [0:, 0]
c2 = matrix [0:, 1]
c3 = matrix [0:, 2]
c = -1 * (np.column_stack((c1,c2,c3)))
detc = np.linalg.det(c)
rndc = round(detc)

d = matrix [0:, 1:]
detd = np.linalg.det(d)
rnddet = round(detd)

centerx = (-0.5) * (rndx/rnddet)
centery = (-0.5) * (rndy/rnddet)

rad = rndc/rnddet

radius = ((x1-centerx)**2) + ((y1-centery)**2)
rad = sqrt(radius)
 
print ('')
print ('The Center of the Circle is ', '(', centerx, ',', centery, ')')
print ('The Radius of the Circle is ', rad)

if rndxy != 0:
    xx = rndx/rndxy
    yy = rndy/rndxy
    cc = rndc/rndxy
    
    print ('The Coefficient for the equation of the circle','[', xx, ',', yy, ',', cc, ']')
else:
    print ('The Coefficient for the equation of the circle','[', rndx, ',', rndy, ',', rndc, ']')