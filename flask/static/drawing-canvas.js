import SignaturePad from 'signature_pad';

function DrawingCanvas(element, options) {
    this.element = element;
    this.ctx = element.getContext('2d');
    this.opts = options || {};
    this.signaturePad = new SignaturePad(element, {
        minWidth: 1,
        maxWidth: 1,
        minDistance: 2
    });
}

DrawingCanvas.prototype.clear = function () {
    this.signaturePad.clear();
    return this;
}

DrawingCanvas.prototype.data = function () {
    return this.ctx.getImageData(0, 0, this.ctx.canvas.width, this.ctx.canvas.height);
}

export default DrawingCanvas;