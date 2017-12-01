from keras.models import load_model

cnn_digit_clf = load_model("../ML_model/cnn_digit_clf.h5")

def predict(processedData):
    predictedLabel = cnn_digit_clf.predict_classes([processedData])
    return predictedLabel
