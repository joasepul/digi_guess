import unittest
import sys
sys.path.append('..')
import scipy.misc
from ML_model import preproc
import pickle
import numpy as np

class Test_digit_centering(unittest.TestCase):

    def setUp(self):
        with open("user_digit_test_input.pickle", "rb") as f:
            input_list = pickle.load(f)

        self.userinput_list = input_list

    def test_user_input_processing(self):

        for user_input in self.userinput_list:
            processed = np.array(user_input).reshape((100, 100))
            preproc.display_digit(processed, title="Raw Digit Data")
            processed = preproc.center_matrix(processed, padding=10)
            preproc.display_digit(processed, title="Centered Digit Data")
            self.assertEqual(processed.shape, (100,100))
            processed = scipy.misc.imresize(processed,
                                            (28,28),
                                            interp="lanczos")
            self.assertEqual(processed.shape, (28,28))
            preproc.display_digit(processed, title="Resized to 28x28")
            processed = processed.reshape(1, 1, 28, 28).astype('float32')




if __name__ == '__main__':
    unittest.main()
