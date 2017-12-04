import unittest
import sys
sys.path.append('..')
from preproc import *
import pickle
import numpy as np

tempList = []
class Test_digit_centering(unittest.TestCase):

    def setUp(self):
        with open("user_digit_test_input.pickle", "rb") as f:
            input_list = pickle.load(f)

        self.userinput_list = input_list

    def test_user_input_processing(self):

        for user_input in self.userinput_list:
            processed = np.array(user_input).reshape((100, 100))
            display_digit(processed, title="Raw Digit Data")
            processed = center_matrix(processed, padding=10)
            display_digit(processed, title="Centered Digit Data")
            self.assertEqual(processed.shape, (100,100))
            processed = scipy.misc.imresize(processed,
                                            (28,28),
                                            interp="lanczos")
            self.assertEqual(processed.shape, (28,28))
            display_digit(processed, title="Resized to 28x28")
            processed = processed.reshape(1, 1, 28, 28).astype('float32')
            tempList.append(processed)
        with open("processed_user_data.pickle", "wb") as f:
            pickle.dump(tempList ,f)




if __name__ == '__main__':
    unittest.main()
