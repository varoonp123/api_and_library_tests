import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def func(x,y):
        return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)

#only know 1000 values in a the unit square. Want to interpolate to approximate func continuously

grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]

#generate 1000 random (x,y) points and eval func at those points
points = np.random.rand(1000,2)
values = func(points[:,0], points[:,1])

grid_1 = griddata(points,values,(grid_x, grid_y), method = 'nearest')
grid_2 = griddata(points,values,(grid_x, grid_y), method = 'linear')
grid_3 = griddata(points,values,(grid_x, grid_y), method = 'cubic')


#show results of interpolation methods in subplots

plt.subplot(221)
plt.imshow(func(grid_x,grid_y).T, extent=(0,1,0,1), origin = 'lower')
plt.plot(points[:,0],points[:,1], 'k.',ms=1)
plt.title('Real Vals')


plt.subplot(222)
plt.imshow(grid_1.T, extent=(0,1,0,1), origin = 'lower')
plt.title('Nearest')


plt.subplot(223)
plt.imshow(grid_1.T, extent=(0,1,0,1), origin = 'lower')
plt.title('Linear')

plt.subplot(224)
plt.imshow(grid_1.T, extent=(0,1,0,1), origin = 'lower')
plt.title('Cubic')

plt.gcf().set_size_inches(6,6)
plt.show()
                                                                                                                           


