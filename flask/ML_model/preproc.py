import scipy.misc
import scipy.ndimage
import skimage
import numpy as np
import pickle


def process_matrix(unprocessed):
    processed = np.array(unprocessed).reshape((100, 100))
    # display_digit(processed)
    processed = center_matrix(processed, padding=10)
    # display_digit(processed)
    processed = scipy.misc.imresize(processed, (28,28), interp="lanczos")
    # display_digit(processed)
    processed = processed.reshape(1, 1, 28, 28).astype('float32')
    return processed


def center_matrix(unprocessed, padding=0):
    min_y, min_x, max_y, max_x = get_bounding_box(unprocessed,
                                                  padding=padding)
    digit_sub_matrix = unprocessed[min_y:max_y, min_x:max_x]
    digit_sub_matrix = scipy.misc.imresize(digit_sub_matrix,
                                           size=(100, 100),
                                           interp='lanczos')

    return digit_sub_matrix
    # now center -> resize -> pad back up to 100


def display_digit(digit, title = ""):
    import matplotlib
    import matplotlib.pyplot as plt
    plt.title(title)
    plt.imshow(digit,
               cmap=matplotlib.cm.binary)
    plt.show()


def floor_even(number):
    if number % 2 != 0:
        return number - 1
    return number


def ciel_even(number):
    if number % 2 != 0:
        return number + 1
    return number


def get_bounding_box(np_matrix, padding=0):
    min_x = np_matrix.shape[1]
    min_y = np_matrix.shape[0]
    max_x = 0
    max_y = 0
    zero_row = np.zeros((100,), dtype=np.float32)
    for y_index, row in enumerate(np_matrix):  # Y axis
        if not np.array_equal(row, zero_row):
            if min_y > y_index:
                min_y = y_index
            if max_y < y_index:
                max_y = y_index
        for x_index, elem in enumerate(row):  # X axis
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
        min_y = y_center - x_diff // 2
        max_y = y_center + x_diff // 2
    else:
        min_x = x_center - y_diff // 2
        max_x = x_center + y_diff // 2

    min_x = max(min_x - padding, 0)
    min_y = max(min_y - padding, 0)
    max_x = min(max_x + padding, 100)
    max_y = min(max_y + padding, 100)

    return min_y, min_x, max_y, max_x
