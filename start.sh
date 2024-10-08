yolo task=detect mode=train model=yolov8l.yaml data=../datasets/data.yaml epochs=200 batch=128 device=\'0,1,2,3,4,5,6,7\'
yolo task=detect mode=val model=runs/detect/train2/weights/best.pt  data=../datasets/data.yaml device=cpu
yolo task=detect mode=predict model=ultralytics/yolo/v8/detect/runs/detect/train5/weights/best.pt source=../datasets/images/val  device=cpu

yolo task=detect mode=train model=yolov8x.pt data=../datasets/data.yaml batch=128 epochs=300 imgsz=640 workers=16 device=\'0,1,2,3,4,5,6,7\'
