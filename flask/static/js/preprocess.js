export function simplifyArray(imageArr) {
    if (imageArr.length % 4 !== 0) {
        throw new PreprocessingException('invalid image data array length');
    }
    const simpleArr = imageArr.filter(
        (value, index) => (index + 1) % 4 == 0);
    return Array.from(simpleArr)
}

function PreprocessingException(message) {
    this.message = message;
    this.name = 'PreprocessingException';
}
