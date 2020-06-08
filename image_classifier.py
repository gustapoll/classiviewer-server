from keras.models import load_model
from keras.preprocessing import image
# from sklearn.metrics import classification_report, confusion_matrix
from keras.models import load_model
import os
import numpy as np
import pandas as pd

from os import path
root = path.dirname(path.abspath(__file__))

model = load_model(path.join(root, 'models/0.8732057416267942_1568206179.5820658.h5'))
model._make_predict_function() 

def id2label(id):
    
    if id == 1:
        cat = "ID"
    elif id == 2:
        cat = "F"
    elif id == 3:
        cat = "IM"
    elif id == 4:
        cat = "TD"
    elif id == 5:
        cat = "TV"
    else:
        cat = "UKN"
    
    return cat

def predict(image_files, classifier=model):
    # Load Images
    X_test = []
    X_img = []
    for img in image_files:

        im = image.load_img("./images/" + img, target_size=(120,120,1), grayscale=False)
        im_arr = image.img_to_array(im)
        im_arr = im_arr/255
        X_img.append(im)
        X_test.append(im_arr)

    X_test = np.array(X_test)

    y_pred = model.predict_classes(X_test)

    labeled_df = pd.DataFrame(data=[image_files, y_pred]).T
    labeled_df.columns = ['name', 'label']
    labeled_df['label'] = labeled_df['label'].apply(id2label)

    return labeled_df.to_dict('records')
