import scipy.misc
import scipy.ndimage
import numpy as np


def process_matrix(unprocessed):
    processed = np.array(unprocessed, dtype=np.uint8).reshape((100,100))
    processed = center_matrix(processed)
    processed = scipy.misc.imresize(processed, (28,28), interp="lanczos")
    processed = processed.reshape(1, 1, 28, 28).astype('float32')
    return processed


def displayDigit(digit):
    import matplotlib
    import matplotlib.pyplot as plt
    plt.imshow(digit, cmap = matplotlib.cm.binary)
    plt.show()

def floor_even(number):
    if number % 2 != 0:
        return number - 1
    return number

def ciel_even(number):
    if number % 2 != 0:
        return number + 1
    return number

def center_matrix(unprocessed):
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


    min_x = floor_even(min_x)
    min_y = floor_even(min_y)
    max_x = ciel_even(max_x)
    max_y = ciel_even(max_y)
    x_diff = max_x - min_x
    y_diff = max_y - min_y
    x_center = (max_x + min_x) // 2
    y_center = (max_y + min_y) // 2

    if x_diff > y_diff:
        min_y = max(y_center - x_diff // 2, 0)
        max_y = min(y_center + x_diff // 2, 100)
    else:
        min_x = max(x_center - y_diff // 2, 0)
        max_x = min(x_center + y_diff // 2, 100)

    digit_sub_matrix = unprocessed[min_y:max_y, min_x:max_x]

    digit_sub_matrix = scipy.misc.imresize(digit_sub_matrix, size=(100, 100), interp='lanczos')

    return digit_sub_matrix
    # now center -> resize -> pad back up to 100
