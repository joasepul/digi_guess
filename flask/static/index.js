// var io = require('socket.io-client');
import DrawingCanvas from './drawing-canvas';
import $ from 'jquery';
// var socket = io.connect('http://127.0.0.1:5000');
// socket.on('connect', function() {
//     socket.emit('init', {data: 'I\'m connected!'});
// });

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
        },
        error: function() {
            console.log('ajax request failed');
        }
    });
    // socket.emit('preproc', {data: simplifyArray(imageData.data)});
});

document.querySelector('#clear-button').addEventListener("click", function(e) {
    drawingCanvas.clear();
});