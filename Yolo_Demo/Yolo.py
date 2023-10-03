from ultralytics import YOLO 
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

""" This quick YOLOv8 Demo is based on this Github Link https://github.com/ultralytics/ultralytics/blob/main """

# load the pretrained model
model = YOLO("yolov8s.pt")

# connect camera 
results = model.predict(source="0", show=True)

print(results)