var canvas = document.querySelector('canvas');
var ctx = canvas.getContext("2d");

var clickX = [];
var clickY = [];
var clickDrag = [];
var drawing;

function clearCanvas() {
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}

function addClick(x, y, dragging) {
    clickX.push(x);
    clickY.push(y);
    clickDrag.push(dragging);
}

function redraw() {
    clearCanvas();
    ctx.strokeStyle = "#000000";
    ctx.lineJoin = "round";
    ctx.lineWidth = 5;

    clickX.forEach(function(click, i) {
        ctx.beginPath();
        if (clickDrag[i] && i) {
            ctx.moveTo(clickX[i-1], clickY[i-1]);
        } else {
            ctx.moveTo(clickX[i] - 1, clickY[i]);
        }
        ctx.lineTo(clickX[i], clickY[i]);
        ctx.closePath();
        ctx.stroke();
    });
}

canvas.addEventListener("mousedown", function(e) {
    var mouseX = e.pageX - this.offsetLeft - this.offsetParent.offsetLeft;
    var mouseY = e.pageY - this.offsetTop - this.offsetParent.offsetTop;
    drawing = true;
    addClick(mouseX, mouseY);
    redraw();
});

canvas.addEventListener("mousemove", function(e) {
    if (drawing) {
        var mouseX = e.pageX - this.offsetLeft - this.offsetParent.offsetLeft;
        var mouseY = e.pageY - this.offsetTop - this.offsetParent.offsetTop;
        addClick(mouseX, mouseY);
        redraw();
    }
});

canvas.addEventListener("mouseup", function(e) {
    drawing = false;
});

canvas.addEventListener("mouseleave", function(e) {
    drawing = false;
});

document.querySelector('#clear-button').addEventListener("click", function(e) {
    clearCanvas();
    clickX = [];
    clickY = [];
    clickDrag = [];
});

document.querySelector('#submit-button').addEventListener("click", function(e) {
    var imageData = ctx.getImageData(0, 0, ctx.canvas.width, ctx.canvas.height);
    console.log(imageData);
});

