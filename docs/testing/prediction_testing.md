# Model Prediction Module
## Module 'model' in ML_model package
### Expected behavior:
	Usage: 
		from ML_model import model
		predicted_label = model.predict(processed_matrix)
	Input:
		processed_matrix is a 28*28 size matrix that has been centered
		and shrunk down from the original canvas size of 100*100.
	Output:
		A digit from 0 to 9 representing the lable the trained
		model predicted.
### Method of testing:
	We used the python module unittest which contains a list of 10 processed
	matrices. We predict each one, and assert the equality between the 
	predicted label and true label. Due to the nature of classification, 
	any input of the size 28*28 is legal and predicted. The only illegal input is
	a data of the wrong size.
