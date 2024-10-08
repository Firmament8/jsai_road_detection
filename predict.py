from ultralytics import YOLO
# import argparse
# parser = argparse.ArgumentParser(description = 'YOLO detect')
# parser.add_argument('--image_path', '-i', type = str, default = './data/images', help = '图片路径')
# parser.add_argument('--txt_path', '-t', type = str, default = './data/txt', help = 'txt保存路径')
# args = parser.parse_args()
 
model = YOLO("rectangle.pt")
# model.predict(source="./images", iou=0.25, conf=0.2, save=False, save_conf=False, save_txt=True, name='output')
# 0.3
# model.predict(source="./images", iou=0.35, conf=0.25, save=False, save_conf=False, save_txt=True, name='output')
# 0.281
# model.predict(source="./images", iou=0.35, conf=0.20, save=False, save_conf=False, save_txt=True, name='output', max_det=10, agnostic_nms=True)
# 0.295
# model.predict(source="./images", iou=0.25, conf=0.20, save=False, save_conf=False, save_txt=True, name='output', max_det=10, agnostic_nms=True)
# 0.288
model.predict(source="./images", save=True, save_conf=False, save_txt=True,name='output')
#0.302

# model.predict(source="./images", iou=0.35, conf=0.20, save=False, save_conf=False, save_txt=True, name='output',device='0')
#l模型0.308   x扩增

# def predict(source : str = args.image_path, txt_path : str = args.txt_path):
#     model = YOLO("best_6.pt")
#     model.predict(source=source, iou=0.35, conf=0.20, save=False, save_conf=False, save_txt=True, name=txt_path,
#                   device='0')
#
# if __name__ == '__main__':
#     predict()