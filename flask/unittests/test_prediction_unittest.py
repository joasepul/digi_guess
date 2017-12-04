import unittest
import sys
sys.path.append('..')
from model import predict
import pickle

class Test_digit_centering(unittest.TestCase):

    def setUp(self):
        with open("processed_user_data.pickle", "rb") as f:
            input_list = pickle.load(f)

        self.preproc_data_list = input_list
        self.label_list = [1,2,3,4,5,6,7,8,9,0]

    def test_user_input_processing(self):

        for index, preproc_data in enumerate(self.preproc_data_list):
            predicted_label = predict(preproc_data)
            self.assertEqual(predicted_label, self.label_list[index])




if __name__ == '__main__':
    unittest.main()
