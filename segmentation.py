from ultralytics import YOLO #Zmodyfikonany YOLO z ultralytics - brak wyświetlania bounding boxów, zmienione zachowanie dotyczące parametru line_width
import torchvision.transforms as T
import numpy as np
import cv2

class Segmentation:
    def __init__(self):
        self.model = YOLO("yolov8m-seg.pt")
        
    def get_image(self, img):
        results = list(self.model(img, conf=0.128))
        results_classes_counts = {}
        for r in results:
            for c in r.boxes.cls:
                if self.model.names[int(c)] in results_classes_counts:
                    results_classes_counts[self.model.names[int(c)]] += 1
                else:
                    results_classes_counts[self.model.names[int(c)]] = 1
        return T.ToPILImage()(results[0].plot(line_width = 0)), results_classes_counts

    
