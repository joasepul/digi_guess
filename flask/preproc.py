import scipy.misc
import scipy.ndimage
import numpy as np


def process_matrix(unprocessed):
    processed = np.array(unprocessed, dtype=np.uint8).reshape((100,100))
    center_matrix(processed)
    processed = scipy.misc.imresize(processed, (28,28), interp="nearest")
    processed = processed.reshape(1, 1, 28, 28).astype('float32')
    return processed


def center_matrix(unprocessed):
    # find min row, min col
    # find max row, max col
    # pad a lil
    return_matrix = np.zeros(unprocessed.shape, dtype=np.uint8)
    matrix_size_y = unprocessed.shape[0]
    matrix_size_x = unprocessed.shape[1]

    min_x = 100
    min_y = 100
    max_x = 0
    max_y = 0
    zero_Row = np.zeros((100,), dtype=np.uint8)
    for y_index, row in enumerate(unprocessed): #Y axis
        if not np.array_equal(row, zero_Row):
            if min_y > y_index:
                min_y = y_index
            if max_y < y_index:
                max_y = y_index
        for x_index, elem in enumerate(row): #X axis
            if elem != 0:
                if min_x > x_index:
                    min_x = x_index
                if max_x < x_index:
                    max_x = x_index

    print("min_x:{0} min_y:{1} max_x:{2} max_y:{3}".format(min_x, min_y, max_x, max_y))

    x_ratio = (max_x - min_x) / matrix_size_x
    y_ratio = (max_y - min_y) / matrix_size_y
    print("x_ratio:{0} y_ratio{1}".format(x_ratio, y_ratio))
    zoom_factor = 1 / (x_ratio if x_ratio > y_ratio else y_ratio)
    digit_sub_matrix = unprocessed[min_y:max_y, min_x:max_x]
    print(digit_sub_matrix.shape)
    digit_sub_matrix = scipy.misc.imresize(digit_sub_matrix, size=zoom_factor)
    np.set_printoptions(threshold=np.nan)
    print(digit_sub_matrix)
    #find center x and y 
    # now center -> resize -> pad back up to 100
