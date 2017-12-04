export function simplifyArray(imageArr) {
    const simpleArr = imageArr.filter(
        (value, index) => (index + 1) % 4 == 0);
    return Array.from(simpleArr)
}
