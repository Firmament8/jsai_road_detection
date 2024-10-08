import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
data = [522, 3107, 278, 323, 407, 555, 3354, 258]
labels = ['横向裂缝', '纵向裂缝', '块状裂缝', '龟裂', '坑槽','修补网状裂缝','修补裂缝','修补坑槽']

plt.bar(range(len(data)), data, tick_label=labels)
plt.show()