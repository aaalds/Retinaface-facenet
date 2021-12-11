import os
import cv2

# 图像路径
im_dir = 'H:\\test'
# 输出视频路径
video_dir = 'E:\\桌面'
##不存在就造一个！
if not os.path.exists(video_dir):
    os.makedirs(video_dir)
# 设置视频帧率
fps = 15  ###设置所需的帧率
# 得到当前路径的所有的文件的列表
frames = sorted(os.listdir(im_dir))
# 得到图像的长、宽
img = cv2.imread(os.path.join(im_dir, frames[0]))
img_size = (img.shape[1], img.shape[0])
# 对路径的常用处理手段，即将路径‘/’分隔开成为一个列表，-1表示取得最右边的数值，在这里就指的是文件名字
seq_name = os.path.dirname(im_dir).split('/')[-1]
# 设置视频的新路径+视频格式名字
video_dir = os.path.join(video_dir, seq_name + '.avi')
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
# also can write like:fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# if want to write .mp4 file, use 'MP4V'
##转成视频的核心代码！！注意顺序！
videowriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)

for frame in frames:
    f_path = os.path.join(im_dir, frame)
    image = cv2.imread(f_path)
    videowriter.write(image)
    print(frame + " has been written!")

videowriter.release()