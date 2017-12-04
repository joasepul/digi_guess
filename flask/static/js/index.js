import DrawingCanvas from './drawing-canvas';
import $ from 'jquery';
import {simplifyArray} from './preprocess';

const canvas = document.querySelector('canvas');
const drawingCanvas = new DrawingCanvas(canvas);
const ctx = canvas.getContext('2d');

document.querySelector('#submit-button').addEventListener("click", function(e) {
    if (drawingCanvas.isDisplayingResult || drawingCanvas.isEmpty()) {
        return;
    }
    var imageData = simplifyArray(drawingCanvas.data());
    $.ajax({
        url: '/get_digit',
        type: 'POST',
        data: JSON.stringify(imageData),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data) {
            drawingCanvas.clear();
            drawingCanvas.writeDigit(data);
            drawingCanvas.isDisplayingResult = true;
        },
        error: function() {
            console.log('ajax request failed');
        }
    });
});

document.querySelector('#clear-button').addEventListener("click", function(e) {
    drawingCanvas.clear();
});
