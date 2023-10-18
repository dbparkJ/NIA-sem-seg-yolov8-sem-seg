from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')  # load a pretrained model (recommended for training)
if __name__ == '__main__':
    model.train(
        data=r'D:\data\model.yaml',
        epochs=30,
        batch=32,
        device=0,
        name='AI_HUB_yolov8n-seg'
    )
