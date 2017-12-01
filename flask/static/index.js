import DrawingCanvas from './drawing-canvas';
import $ from 'jquery';

var canvas = document.querySelector('canvas');

function simplifyArray(imageArr) {
    var simpleArr = imageArr.filter(
        (value, index) => (index + 1) % 4 == 0);
     simpleArr = simpleArr.map(
         value => {
             if(value > 150){
                 return 1;
             }else{
                 return 0;
             }

         });
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
