from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

def detectskin(img,model):

    # load the saved model
    model = load_model(model)

    # load the test image
    test_image = image.load_img(img, target_size=(224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    # predict the class of the test image
    prediction = model.predict(test_image)

    # print the predicted class
    if prediction[0][0] == 0:

        return "benign"
    else:
        return "malignant"
