from ultralytics import YOLO

model = YOLO(r"C:\Users\JM\PycharmProjects\NIA_sem_seg_Project\runs\segment\AI_HUB_yolov8n-seg\weights\best.pt")

model.predict(
    source="",
    stream=True,
    save=True,
    save_conf=True,
    conf=0.4,
    vid_writer=".mp4"
)