import scipy.misc
import scipy.ndimage
import numpy as np


def processMatrix(unprocessed):
    processed = np.array(unprocessed, dtype=np.uint8).reshape((100,100))
    centerMatrix(processed)
    processed = scipy.misc.imresize(processed, (28,28), interp="nearest")
    processed = processed.reshape(1, 1, 28, 28).astype('float32')
    return processed


def centerMatrix(unprocessed):
    # find min row, min col
    # find max row, max col
    # pad a lil
    returnMatrix = np.zeros(unprocessed.shape, dtype=np.uint8)
    matrix_size_y = unprocessed.shape[0]
    matrix_size_x = unprocessed.shape[1]

    minX = 100
    minY = 100
    maxX = 0
    maxY = 0
    zero_Row = np.zeros((100,), dtype=np.uint8)
    for y_index, row in enumerate(unprocessed): #Y axis
        if not np.array_equal(row, zero_Row):
            if minY > y_index:
                minY = y_index
            if maxY < y_index:
                maxY = y_index
        for x_index, elem in enumerate(row): #X axis
            if elem != 0:
                if minX > x_index:
                    minX = x_index
                if maxX < x_index:
                    maxX = x_index

    print("minX:{0} minY:{1} maxX:{2} maxY:{3}".format(minX, minY, maxX, maxY))

    x_ratio = (maxX - minX) / matrix_size_x
    y_ratio = (maxY - minY) / matrix_size_y
    print("x_ratio:{0} y_ratio{1}".format(x_ratio, y_ratio))
    zoom_factor = 1 / (x_ratio if x_ratio > y_ratio else y_ratio)
    digit_subMatrix = unprocessed[minY:maxY, minX:maxX]
    print(digit_subMatrix.shape)
    digit_subMatrix = scipy.misc.imresize(digit_subMatrix, size=zoom_factor)
    np.set_printoptions(threshold=np.nan)
    print(digit_subMatrix)
    #find center x and y 
    # now center -> resize -> pad back up to 100
