import {simplifyArray} from '../preprocess';

describe("simplifyArray", function() {
    it("gets rid of color information in an array of pixels", function() {
        let testArray, simplifiedArray;

        testArray = [0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255];
        simplifiedArray = [255, 255, 255];
        expect(simplifyArray(testArray)).toEqual(simplifiedArray);

        testArray = [23, 53, 111, 255, 200, 200, 0, 250];
        simplifiedArray = [255, 250];
        expect(simplifyArray(testArray)).toEqual(simplifiedArray);

        testArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        simplifiedArray = [0, 0, 0];
        expect(simplifyArray(testArray)).toEqual(simplifiedArray);

        testArray = [0, 20, 0, 200, 12, 15, 0, 0, 21, 21, 21, 21];
        simplifiedArray = [200, 0, 21];
        expect(simplifyArray(testArray)).toEqual(simplifiedArray);
    });

    it("doesn't accept arrays whose lengths aren't divisible by 4", function() {
        let testArray;

        testArray = [];
        expect(function(){simplifyArray(testArray);}).not.toThrow();

        testArray = [0, 0, 0, 0];
        expect(function(){simplifyArray(testArray);}).not.toThrow();

        testArray = [0, 0];
        expect(function(){simplifyArray(testArray);}).toThrow();

        testArray = [0, 0, 0, 0, 0, 0, 0, 0];
        expect(function(){simplifyArray(testArray);}).not.toThrow();
    })
});