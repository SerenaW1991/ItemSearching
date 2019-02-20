import tensorflow as tf
import cv2
import sys, math
import numpy as np

sys.path.append("/Users/tengwang/Documents/GitHub/ItemSearching/useTensorFlow/models/research/object_detection/")
sys.path.append("/Users/tengwang/Documents/GitHub/ItemSearching/useTensorFlow/models/research/")

from utils import visualization_utils as vis_util

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt

from funcs.func_getColorRatio import *

def inferImage(imagePath, detection_graph, rB, rG, rR, DELTA):
    # Object detection
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            image_np = cv2.imread(imagePath)
            HEIGHT, WIDTH, DEPTH = image_np.shape

            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            # Extract image tensor
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Extract detection boxes
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Extract detection scores
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            # Extract detection classes
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            # Extract number of detectionsd
            num_detections = detection_graph.get_tensor_by_name(
                'num_detections:0')
            # Actual detection.
            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})
            
            for x in range(0, len(boxes[0])):
                # [Y_min, X_min, Y_max, X_max]
                tmpB, tmpG, tmpR = func_getColorRatio(image_np, int(boxes[0][x][1]*WIDTH), int(boxes[0][x][3]*WIDTH), 
                        int(boxes[0][x][0]*HEIGHT), int(boxes[0][x][2]*HEIGHT))
                if(math.fabs(tmpB-rB) > DELTA or math.fabs(tmpG-rG) > DELTA or math.fabs(tmpR-rR) > DELTA):
                    boxes[0][x] = [0,0,0,0]
                
            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                dict(),
                use_normalized_coordinates=True,
                line_thickness=10)

            # Display output
            while True:
                cv2.imshow('object detection', cv2.resize(image_np, (800, 600)))

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break