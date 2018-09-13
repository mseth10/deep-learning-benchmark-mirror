import os

def getImagenetData(dataset):
	if 'ebs' in dataset:
		if not os.path.exists(os.path.expanduser('~/data/')):
			os.system('mkdir -p ~/data/')
			c = os.system("aws s3 sync s3://aws-ml-platform-datasets/imagenet/pass-through/ ~/data/ --exclude \"train*\"")
			print('Downloaded data. Status %d'%c)
	else:
		if not os.path.exists(os.path.expanduser('/media/ramdisk/data/')):
			os.system('mkdir -p /media/ramdisk/data/')
			c = os.system("aws s3 sync s3://aws-ml-platform-datasets/imagenet/pass-through/ /media/ramdisk/data/")
			print('Downloaded data. Status %d'%c)

