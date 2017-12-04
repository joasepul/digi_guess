# Data Preprocessing Module
## Module 'preproc' in ML_model package
### Expected behavior:
	Usage: 
		from ML_model import preproc
		processed_data = preproc.process_matrix(unprocessed_data)
	Input:
		It takes in an unprocessed array size 10000 representing a 
		100*100 user drawn canvas.
	Output:
		It outputs a centered & shrunk down processed matrix size 28*28. 
### Method of testing:
	We used the python module unittest, with a 10 element list of user input.
	The classes tested are every digit from 0-9, a digit written in the corner, 
	edges, and center. It doesn't do anything for an empty matrix. Due to the nature
	of handwritten digits, everything is a legal input. The way we tested if each
	feature within the preprocessing works is by plotting and showing the matrix at 
	three steps: in it's raw unprocessed form, after centering, and after shrinking
	down to 28*28. At any step, if the size is wrong, the test fails.
