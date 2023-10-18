from ultralytics import YOLO

model = YOLO('yolov8l-seg.pt')  # load a pretrained model (recommended for training)
if __name__ == '__main__':
    model.train(
        data=r'D:\data\model.yaml',
        epochs=100,
        batch=8,
        workers=24
    )
