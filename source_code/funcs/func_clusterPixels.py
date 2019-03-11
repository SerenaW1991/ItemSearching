from pandas import DataFrame
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
import numpy as np

import time
from funcs.Color import *

""" func_clusterPixels: use k-means to calculate the color ratio of the image """

def func_clusterPixels(image, k):
	start = time.time()

	B, G, R = [],[],[]
	imgRow, imgCol, _= image.shape
	numPix = imgRow * imgCol
	
	for row in range(0, imgRow):
		for col in range(0, imgCol):
			curB, curG, curR = image[row][col]
			B.append(curB)
			G.append(curG)
			R.append(curR)

	Data = {'B':B, 'G':G, 'R':R}
	df = DataFrame(Data,columns=['B', 'G', 'R'])

	kmeans = KMeans(n_clusters=k).fit(df)
	centroids = kmeans.cluster_centers_
	# domanColor = []

	# for center in centroids:
	# 	domanColor.append(Color(center[0], center[1], center[2]))
		
	domanColorRatio = {}

	for i in range(kmeans.n_clusters):
		a = np.where(kmeans.labels_ == i)
		domanColorRatio.update({i:1.0*len(a[0])/numPix})
		# domanColorRatio.update({domanColor[i]:1.0*len(a[0])/numPix})

	print ("Clustering time: ", time.time()-start)
	print ("Color centers: ", centroids)
	print ("domain color ratio in pattern image: ", domanColorRatio)
	return [kmeans, domanColorRatio]


def plot(B,G,R,kmeans,centroids):
	fig = plt.figure()
	ax = Axes3D(fig)
	ax.scatter(B, G, R, c= kmeans.labels_.astype(float), alpha=0.5)
	ax.scatter([centroids[0][0]],[centroids[0][1]],[centroids[0][2]],color='red')
	ax.scatter([centroids[1][0]],[centroids[1][1]],[centroids[1][2]],color='red')
	ax.scatter([centroids[2][0]],[centroids[2][1]],[centroids[2][2]],color='red')
	
	plt.show()