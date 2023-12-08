from ultralytics import YOLO

model = YOLO('yolov8x-seg.pt')  # load a pretrained model (recommended for training)
if __name__ == '__main__':
    model.train(
        data=r'D:\data\model.yaml',
        epochs=200,
        batch=64,
        device=[0,1,2,3],
        name='AI_HUB_yolov8x-seg_batch64_200'
    )
