# Front-End Preprocessing Module
## Module 'preprocessing' in flask/static/js
### Expected behavior:
	Usage: 
		import {simplifyArray} from './preprocess';
		simplifyArray(imageData);
	Input:
		Single dimensional array of color data (rgba) for each pixel in the canvas element
	Output:
		Single dimensional array containing only the 'a' data for each pixel
### Method of testing:
	Automated unit tests using Jasmine which tests several example input arrays.
