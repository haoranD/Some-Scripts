import os

path = '/home/haoran/A-LivenessDetection/LivenessDetection-master/Data/webface/'


count = 0

for file in os.listdir(path):
    newname=str(count)
    os.rename(os.path.join(path,file),os.path.join(path,newname))
    print (count)
    count = count + 1
