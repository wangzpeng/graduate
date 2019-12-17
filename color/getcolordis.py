import cv2

origin_color=[7525,21890,32857,24472,21636,25623,10226,6774,4450,11047]
f=open('color.txt','r')
lines=f.readlines()
res=[]
for line in lines:
	line=line.strip().split()
	nm=line[0]
	v=line[1].split(',')
	d=0
	for i in range(10):
		d+=abs(int(v[i])-origin_color[i])
	res.append((d,nm))
res=sorted(res)
for i in range(10):
	img_nm=res[i][1]
	img=cv2.imread(r'G:\tftest\tf-faster-rcnn-master\tf-faster-rcnn\tf-faster-rcnn\data\VOCdevkit2007\VOC2007\JPEGImages\\'+img_nm)
	cv2.imwrite(r"G:\tftest\tf-faster-rcnn-master\tf-faster-rcnn\tf-faster-rcnn\data\VOCdevkit2007\VOC2007\results\000556\000556_2\\"+str(i)+'_'+img_nm,img)
	cv2.waitKey()