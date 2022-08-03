import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np
from numpy import linalg

if(True):
    curstate = [np.array([[0.8],[0.1],[0.1]]),
            np.array([[0.3],[0.4],[0.3]]),
            np.array([[0.6],[0.3],[0.1]])]
    # rps = np.array([[0,-1,1],
    #         [1,0,-1],
    #         [-1,1,0]])
    rps = np.array([[0,-1,1],
            [1,0,-2],
            [-1,2,0]])
else:
    rps = np.array([1]) #old version
    curstate = [np.array([60.0]), np.array([0.0]), np.array([0.0])]

iterations = 1000
numagent = 3

energy = []
# log = [[] for i in range(numagent)]

eta = 0.4 #hyperparameter learning rate. Setting it to 0.5 w/
#scissor-paper doubling makes it explode (kaboom!)

# print(np.transpose(curstate[0]))
# print(np.matmul(rps,curstate[1]))
# # print(curstate[0] * np.transpose(np.matmul(rps,curstate[1])))
# print(np.transpose(curstate[0]) * np.matmul(rps,curstate[1]))
# print(float(np.transpose(curstate[0]) * np.matmul(rps,curstate[1])))
# print(float(np.matmul(np.transpose(curstate[0]), np.matmul(rps,curstate[1]))))

print("end testing\n")

totalavg = [curstate[i]/(iterations+1) for i in range(numagent)]
for t in range(iterations):
    for i in range(numagent):
        for j in range(i): #j<i
            curstate[i] -= eta * np.matmul(np.transpose(rps),curstate[j])
        for j in range(i+1,len(curstate)): #j>i
            curstate[i] += eta * np.matmul(rps,curstate[j])
        # log[i].append(curstate[i].copy)
        print(f"{i}: {curstate[i]}")
        totalavg[i] += curstate[i]/(iterations+1)
    p1=sum([(linalg.norm(curstate[i])**2)/eta for i in range(numagent)])
    if(curstate[0].shape[0]>1):
        p2=sum([sum([float(np.matmul(np.transpose(curstate[i]), np.matmul(rps,curstate[j]))) for i in range(j)]) for j in range(numagent)])
    else:
        p2=sum([sum([float(np.transpose(curstate[i]) * np.matmul(rps,curstate[j])) for i in range(j)]) for j in range(numagent)])
    energy.append(p1+p2)


for t in range(iterations):
    # print(f"iteration: {t}")
    # for i in range(numagent):
    #     print(log[i][t])
    print(f"energy at {t}: {energy[t]}")
print(f"min: {min(energy)}, max: {max(energy)}")

for i in range(numagent):
    print(totalavg[i])
