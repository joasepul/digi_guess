import SignaturePad from 'signature_pad';

function DrawingCanvas(element, options) {
    this.element = element;
    this.ctx = element.getContext('2d');
    this.opts = options || {};
    this.signaturePad = new SignaturePad(element, {
        minWidth: 3,
        maxWidth: 3,
        minDistance: 5
    });
}

DrawingCanvas.prototype.clear = function () {
    this.signaturePad.clear();
    return this;
}

DrawingCanvas.prototype.data = function () {
    return this.ctx.getImageData(0, 0, this.ctx.canvas.width, this.ctx.canvas.height).data;
}

DrawingCanvas.prototype.writeDigit = function(digit) {
    this.ctx.font = '2em sans-serif';
    this.ctx.textAlign = 'center';
    this.ctx.textBaseline = 'middle';
    this.ctx.fillText(digit, this.element.width/2, this.element.height/2);
}

export default DrawingCanvas;
