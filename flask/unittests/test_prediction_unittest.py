import unittest
import sys
sys.path.append('..')
from ML_model import model
import pickle

class Test_prediction(unittest.TestCase):

    def setUp(self):
        with open("processed_user_data.pickle", "rb") as f:
            input_list = pickle.load(f)

        self.preproc_data_list = input_list
        self.label_list = [1,2,3,4,5,6,7,8,9,0]

    def test_user_input_processing(self):

        for index, preproc_data in enumerate(self.preproc_data_list):
            true_label = self.label_list[index]
            predicted_label = model.predict(preproc_data)
            print("prediction:{0} true_label:{1}".format(predicted_label,
                                                        true_label))
            self.assertEqual(predicted_label, true_label)




if __name__ == '__main__':
    unittest.main()
