# import classes and functions 

from keras.models import Sequential 
from keras.layers.core import Dense, Activation
from keras.layers import Convolution2D, MaxPooling2D,Dropout, Flatten
from keras.utils import np_utils
from PIL import Image
import os,sys
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from array import array
import numpy as np 
import matplotlib.pyplot as plot
np.random.seed(0)  #for reproducibility 

