var io = require('socket.io-client');
import DrawingCanvas from './drawing-canvas';
var socket = io.connect('http://127.0.0.1:5000');
socket.on('connect', function() {
    socket.emit('init', {data: 'I\'m connected!'});
});

var canvas = document.querySelector('canvas');

function simplifyArray(imageArr) {
    var simpleArr = imageArr.filter(
        (value, index) => (index + 1) % 4 == 0);
    simpleArr = simpleArr.map(
        value => value / 255);
    return Array.from(simpleArr)
}

const drawingCanvas = new DrawingCanvas(canvas);

document.querySelector('#submit-button').addEventListener("click", function(e) {
    var imageData = drawingCanvas.data();
    console.log(simplifyArray(imageData.data));
    socket.emit('preproc', {data: simplifyArray(imageData.data)});
});

document.querySelector('#clear-button').addEventListener("click", function(e) {
    drawingCanvas.clear();
});