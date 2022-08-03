import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np

rps = np.array([[0,-1,1],[1,0,-1],[-1,1,0]])


iterations = 1000
numagent = 3

log = [[] for i in range(numagent)]

curstate = [np.array([[0.4],[0.3],[0.3]]),
			np.array([[0.3],[0.4],[0.3]]),
			np.array([[0.3],[0.3],[0.4]])]

eta = 0.01 #hyperparameter learning rate
for t in range(iterations):
	for i in range(len(curstate)):
		for j in range(i): #j<i
			curstate[i] -= eta * np.matmul(rps,curstate[j])
		for j in range(i+1,len(curstate)): #j>i
			curstate[i] += eta * np.matmul(rps,curstate[j])
		log[i].append(curstate[i])


fig = plt.figure()
if (numagent==2):
	ax = fig.add_subplot()
if(numagent==3):
	ax = fig.add_subplot(projection='3d')

for t in range(iterations):
	for i in range(numagent):
		print(log[i][t])
	print()

if(numagent==2):
	plt.scatter(x[0],x[1], s=50, c=(1,0,0))
	plt.scatter([x[0][i+1] for i in range(iterations)],[x[1][i] for i in range(iterations)], s=50, c=(0,0,1))
if(numagent==3):
	ax.scatter(log[0])
	ax.scatter(log[1])
	ax.scatter(log[2])

	#
	# y = [[x[j][i] for i in range(iterations)] for j in range(3)]
	# z = [[x[j][i+1] for i in range(points)] for j in range(3)]
	# ax.scatter(y[0],y[1],y[2])
	# ax.scatter(z[0], y[1],y[2])
	# ax.scatter(z[0],z[1], y[2])

# ax = fig.add_subplot(133, projection='3d')

	# u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
	# r=60
	# x = r* np.cos(u)*np.sin(v)
	# y = r* np.sin(u)*np.sin(v)
	# z = r* np.cos(v)
	# ax.plot_wireframe(x, y, z, color="red")
	# ax.set_title("Sphere")

plt.show()
