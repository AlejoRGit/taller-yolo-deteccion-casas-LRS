from ultralytics import YOLO
import os

def train():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data.yaml")

    model = YOLO("yolov8n.pt")

    model.train(
        data=data_path,
        epochs=50,
        imgsz=640,
        batch=16,
        project=os.path.join(base_dir, "models"),
        name="house_detector"
    )

if __name__ == "__main__":
    train()