import DrawingCanvas from './drawing-canvas';
import $ from 'jquery';
import {simplifyArray} from './preprocess';

var canvas = document.querySelector('canvas');
const drawingCanvas = new DrawingCanvas(canvas);

document.querySelector('#submit-button').addEventListener("click", function(e) {
    var imageData = simplifyArray(drawingCanvas.data());
    console.log(imageData);
    $.ajax({
        url: '/get_digit',
        type: 'POST',
        data: JSON.stringify(imageData),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data) {
            console.log('success');
            console.log(data);
            document.getElementById('output').innerText = data[0]
        },
        error: function() {
            console.log('ajax request failed');
        }
    });
});

document.querySelector('#clear-button').addEventListener("click", function(e) {
    drawingCanvas.clear();
});
