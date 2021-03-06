#%matplotlib inline
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
plt.rcParams['figure.figsize']= (16,9)
plt.style.use('ggplot')

#importing the dataset
data = pd.read_csv('age_income.csv')
print(data.shape)
data.head()

#Getting the values and plotting

f1 = data['age'].values
f2 = data['income'].values
Xone = np.array(list(zip(f1)))
Yone = np.array(list(zip(f2)))
X = np.array(list(zip(f1,f2)))
plt.xlabel('age')
plt.ylabel('income')
#plt.scatter(f1,f2,c='blue',s=7)
#plt.title('fig-1')
#fig = plt.figure()
#ax1 = fig.add_subplot(111)
#plt.show()

# Euclidean Distance Calculator
def dist(a,b,ax = 1):
	return np.linalg.norm(a-b, axis = ax)

# Number of clusters
k = 2
C_x = np.random.randint(np.min(Xone),np.max(Xone),size = k)
C_y = np.random.randint(np.min(Yone),np.max(Yone),size = k)
C = np.array(list(zip(C_x,C_y)), dtype = np.float32)
print(C)

#plotting along with the centroids
plt.scatter(f1,f2,c='blue',s=7,label = 'first')
plt.scatter(C_x,C_y,marker = '*',s=200,c='g',label = 'second')
#plt.legend(loc = 'upper left')
#lplt.title('Cluster wih centroids')
#plt.show()
print(len(X))


#K-means
C_old = np.zeros(C.shape)
clusters = np.zeros(len(X))
error = dist(C,C_old,None)

while error!=0:
	for i in range(len(X)):
		distances = dist(X[i], C)
		cluster = np.argmin(distances)
		clusters[i] = cluster
	C_old = deepcopy(C)
	for i in range(k):
		points = [X[j] for j in range(len(X)) if clusters[j] == i]
		C[i] = np.mean(points , axis =0)
	error = dist(C,C_old,None)


colors = ['r','g','b','y','c','m']
fig, ax = plt.subplots()

for i in range(k):
	points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
	ax.scatter(points[:,0], points[:,1], s =7 ,c=colors[i])

ax.scatter(C[:,0],C[:,1],marker = '*',s =200,c='#050505')
plt.show()
		
k_range = range(1,10)
distortions = []

for i in k_range:
	kmeanModel = KMeans(n_clusters = i)
	kmeanModel.fit(X)
	distortions.append(sum(np.min(cdist(X,kmeanModel.cluster_centers_,'euclidean'),axis=1)) /X.shape[0])

fig1 = plt.figure()
ex = fig1.add_subplot(111)
ex.plot(k_range,distortions, 'b*-')

plt.grid(True)
plt.ylim([0,45])
plt.xlabel('Number of clusters')
plt.ylabel('Average distortion')
plt.title('Selecting k with the Elbow Method')
plt.show()






