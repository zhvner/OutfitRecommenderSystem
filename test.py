import tensorflow

from keras.applications.restnet50 import ResNet50, preprocess_input
from keras.layers import GlobalMaxPooling2D

import cv2
import numpy as np
from numpy.linalg import norm


model = ResNet50(weights='imagenet', include_top=False,
                 input_shape=(224, 224, 3))
model.trainable = False

model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])

model.summary()


def extract_feature(img_path, model):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))
    img = np.array(img)
    expand_img = np.expand_dims(img, axis=0)
    pre_img = preprocess_input(expand_img)
    predictions = model.predict(pre_img).flatten()
    normalized = predictions / norm(predictions)
    return normalized
