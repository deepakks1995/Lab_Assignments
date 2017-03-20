from randomFunc import generate_N_random
from discriminantFunc import get_discriminant
from naiveBayes import plot_curve, add_plotting_data, plot_3d_curve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

c1_x = []
c1_y = []
c1_z = []
c2_x = []
c2_y = []
c2_z = []
no_of_data_points = 30
mean_classA = [0,0,0]
mean_classB = [4.5,4.5,4.5]
sigma_classA = [1,1,1]
sigma_classB = [1,1,1]
neta = 0.5

'''
*	This function is to generate data from a  
*	gaussian distribution given variance and mean
*	author: Deepak
'''
def generate_data():
	global c1_x, c1_y, c1_z, c2_x, c2_y, c2_z
	data_classA = []
	data_classB = []
	data_classA = generate_N_random(mean_classA, sigma_classA, 3, no_of_data_points)
	data_classB = generate_N_random(mean_classB, sigma_classB, 3, no_of_data_points)
	c1_x = [x.tolist()[0] for x in data_classA]
	c1_y = [x.tolist()[1] for x in data_classA]
	c1_z = [x.tolist()[2] for x in data_classA]
	c2_x = [x.tolist()[0] for x in data_classB]
	c2_y = [x.tolist()[1] for x in data_classB]
	c2_z = [x.tolist()[2] for x in data_classB]

'''
*	This function is to implement a single update 
*	perceptron learning algorithm
*	author: Deepak
'''
def single_update_perceptron_learning():
	global c1_x, c1_y, c1_z, c2_x, c2_y, c2_z
	itr = 0
	w = np.zeros((4,1))
	x = np.zeros((4,1))
	plt.ion()

	while itr < no_of_data_points:
		x[0][0] = c1_x[itr]
		x[1][0] = c1_y[itr]
		x[2][0] = c1_z[itr]
		x[3][0] = 1

		if (np.matmul(np.transpose(w), x)) <= 0:
			w = w + neta * x
			itr = -1

		x[0][0] = c2_x[0 if itr==-1 else itr]	
		x[1][0] = c2_y[0 if itr==-1 else itr]	
		x[2][0] = c2_z[0 if itr==-1 else itr]	
		x[3][0] = 1

		if (np.matmul(np.transpose(w), x)) > 0:
			w = w - neta * x 
			itr = -1

		itr += 1
	
	x1 = []
	y1 = []
	z1 = []
	for i in np.arange(-2, 7, 0.1):
		for j in np.arange(-2, 7, 0.1):
			x1.append(i)
			y1.append(j)
			z = (w[0][0]*i + w[1][0]*j +  w[3][0])/(-1*w[2][0])
			z1.append(z)
	# Plotting Curves		
	data_classA = []
	data_classB = []
	data = []
	for i in range(len(c1_x)):
		data_classA.append([c1_x[i], c1_y[i], c1_z[i]])	
	for i in range(len(c2_x)):
		data_classB.append([c2_x[i], c2_y[i], c2_z[i]])
	for i in range(len(x1)):
		data.append([x1[i], y1[i], z1[i]])
	add_plotting_data(data_classA, 'o', 'red')
	add_plotting_data(data_classB, 'o', 'blue')
	add_plotting_data(data, 'None', 'green')
	plot_3d_curve("Single Update Perceptron Learning")

if __name__=="__main__":
	generate_data()
	single_update_perceptron_learning()