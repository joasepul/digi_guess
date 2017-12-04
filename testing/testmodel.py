import numpy
import NeuralNetDigitRecon as dig_rec
from keras.models import load_model

# import the model
cnn_model = load_model("../ML_model/cnn_digit_clf.h5")

# test model
grade = cnn_model.evaluate(dig_rec.X_test, dig_rec.y_test, batch_size=1, verbose=0)
print("Large CNN Error: %.2f%%" % (100-grade[1]*100))


