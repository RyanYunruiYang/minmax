import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np


points = 100
numagent = 3
x = [[0 for i in range(points+1)] for i in range(numagent)]

x[0][0] = 60

eta = (3.4)/points

for t in range(points):
	# for j in range(numagent):
	# 	newval = x[j][-1]
	# 	for k in range(numagent):
	# 		if(k!=j):
	# 			newval -= eta * x[k][-1]
	# 	x[j].append(newval)

	if(numagent==2):
		x[0][t+1] = x[0][t] + eta* x[1][t]
		x[1][t+1] = x[1][t] - eta* x[0][t+1]
	if(numagent==3):
		a = 1
		x[0][t+1] = x[0][t] + eta*(a*x[1][t] + x[2][t])
		x[1][t+1] = x[1][t] + eta*(-a*x[0][t+1] + x[2][t])
		x[2][t+1] = x[2][t] + eta*(-x[0][t+1] - x[1][t+1])

fig = plt.figure()
if (numagent==2):
	ax = fig.add_subplot()
if(numagent==3):
	ax = fig.add_subplot(projection='3d')


print(x)

if(numagent==2):
	plt.scatter(x[0],x[1], s=50, c=(1,0,0))
	plt.scatter([x[0][i+1] for i in range(points)],[x[1][i] for i in range(points)], s=50, c=(0,0,1))
if(numagent==3):
	y = [[x[j][i] for i in range(points)] for j in range(3)]
	z = [[x[j][i+1] for i in range(points)] for j in range(3)]
	ax.scatter(y[0],y[1],y[2])
	ax.scatter(z[0], y[1],y[2])
	ax.scatter(z[0],z[1], y[2])

# ax = fig.add_subplot(133, projection='3d')
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
r=60
x = r* np.cos(u)*np.sin(v)
y = r* np.sin(u)*np.sin(v)
z = r* np.cos(v)
ax.plot_wireframe(x, y, z, color="red")
ax.set_title("Sphere")

plt.show()
