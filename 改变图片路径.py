import os
import shutil
path = "./函数与极限" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名

for file in files:
    if file.endswith(".png") or file.endswith(".jpg"):
        shutil.move(path+"/"+file,path + "/pictures")

print(files)
