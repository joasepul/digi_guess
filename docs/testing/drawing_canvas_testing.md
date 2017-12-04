# Drawing Canvas Module
## Module 'drawing-canvas' in flask/static/js
### Creates and manages a drawable canvas element that works with both mouse and touch events
### Usage: 
	  import DrawingCanvas from './drawingCanvas';
### Available Fields and Methods:
    DrawingCanvas(canvasElement, options)
    DrawingCanvas.clear()
    DrawingCanvas.data()
    DrawingCanvas.writeDigit(digit)
    DrawingCanvas.isEmpty()
    DrawingCanvas.isDisplayingResult
### Method of testing:
	Each part of the interface was tested manually. Outputs of each part of the interface were
    observed. The Drawing Canvas module is just an interface that uses another library for the
    actual implementation.
