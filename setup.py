import sys
import os
import glob

current_dir = os.path.dirname(os.path.abspath(__file__))

file_train = open('obj-train.txt', 'w')
file_test = open('obj-test.txt', 'w')

for idx in range(3):
	dirName = os.path.join(current_dir, 'Images', '%03d' % idx)
	imageList = glob.glob(os.path.join(dirName, '*.jpg'))
	for img in imageList:
		file_train.write(img + '\n')
	for img in imageList[:10]:
		file_test.write(img + '\n')


