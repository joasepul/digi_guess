import unittest
import sys
sys.path.append('..')
from preproc import *
import pickle

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



if __name__ == '__main__':
    unittest.main()
