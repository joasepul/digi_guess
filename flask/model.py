from keras.models import load_model

cnn_digit_clf = load_model("../ML_model/cnn_digit_clf.h5")


def predict(processed_data):
    predicted_label = cnn_digit_clf.predict_classes([processed_data])
    return predicted_label
