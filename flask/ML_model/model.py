from keras.models import load_model
import os

model_path = os.path.join(os.path.dirname(__file__), "cnn_digit_clf.h5")
cnn_digit_clf = load_model(model_path)
def predict(processed_data):
    predicted_label = cnn_digit_clf.predict_classes([processed_data])
    return predicted_label[0]
