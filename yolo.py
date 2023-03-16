from ultralytics import YOLO

class Yolo:
    def __init__(self, modeltype):
        if modeltype == 'yolov8n':
            self.model = YOLO("yolov8n.pt")
        elif modeltype == 'yolov8s':
            self.model = YOLO("yolov8s.pt")
        elif modeltype == 'yolov8m':
            self.model = YOLO("yolov8m.pt")
        elif modeltype == 'yolov8l':
            self.model = YOLO("yolov8l.pt")
        elif modeltype == 'yolov8x':
            self.model = YOLO("yolov8x.pt")
        
    def detect(self, img):
        results = self.model(img)
        return results[0].plot()