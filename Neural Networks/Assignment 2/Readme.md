NOTE:
1.	All the files that are generated by programs are in folder output/
2.	Q-3 cannot be run directly from the makefile. It's functions are used as a 
	helper functions in other questions to get random samples from gaussian distribution
3.	The output Images for Question 10 and 11 are 3-dimensional.These images will be displayed
	on the screen for 20 screen. 

HOW TO RUN:

1. To draw Bayesian Decision boundary using a bivariate gaussian distribution in Question-4(a):
	
	make Q4-a

2.	To draw Bayesian Decision boundary from samples generated using different low variance gaussian
	distribution in Question-4(b) type

	make Q4-b

	Note: This program will take approx 5-7 minutes depending on the performance of the processor

3.	For Convergence Study of Perceptron in Question-10 using Single and Batch Update:

	make Q10  

4.	For Convergence Study of Perceptron Using relaxation Update in Question-11 :

	make Q11

5. To run all the programs at the same time

	make full