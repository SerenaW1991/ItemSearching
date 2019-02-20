import os
import sys
import tensorflow as tf
import cv2

from funcs.inferImage import *
from funcs.utils import *
from funcs.func_getColorRatio import *

MODEL_NAME = 'download_models/mask_rcnn_inception_v2_coco_2018_01_28'

# # Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# # Load a (frozen) Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')


DELTA = 0.1
inputImage = cv2.imread("productImage/NyQuil_Severe.jpg")
inputHeight, inputWidth, inputDepth = inputImage.shape
rB, rG, rR = func_getColorRatio(inputImage, 0,inputWidth, 0, inputHeight)
print (rB, rG, rR)
inferImage("testImage/test_complicated.png", detection_graph, rB, rG, rR, DELTA)