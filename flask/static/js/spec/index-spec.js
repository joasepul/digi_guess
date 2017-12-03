import {simplifyArray} from '../preprocess';

describe("simplifyArray", function() {
    it("gets rid of color information in an array of pixels", function() {
        let testArray, simplifiedArray;

        testArray = [0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255];
        simplifiedArray = [1, 1, 1];
        expect(simplifyArray(testArray)).toEqual(simplifiedArray);

        testArray = [23, 53, 111, 255, 200, 200, 0, 250];
        simplifiedArray = [1, 1];
        expect(simplifyArray(testArray)).toEqual(simplifiedArray);

        testArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        simplifiedArray = [0, 0, 0];
        expect(simplifyArray(testArray)).toEqual(simplifiedArray);
    });
});