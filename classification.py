from torchvision.io import read_image
from torchvision.models import resnet50, ResNet50_Weights
from PIL import Image

class Classification:
    def __init__(self):
        # Step 1: Initialize model with the best available weights
        self.weights = ResNet50_Weights.DEFAULT
        self.model = resnet50(weights=self.weights)
        self.model.eval()
        self.preprocess = self.weights.transforms()
    
    def classify(self, img):
        # Step 3: Apply inference preprocessing transforms
        batch = self.preprocess(img).unsqueeze(0)

        # Step 4: Use the model and print the predicted category
        prediction = self.model(batch).squeeze(0).softmax(0)
        class_id = prediction.argmax().item()
        score = prediction[class_id].item()
        category_name = self.weights.meta["categories"][class_id]
        return f"{category_name}: {100 * score:.1f}%"
        
        
        
        