import cv2

img=[(89,89,89,75,101,358,302)]
temp=[([(80,80,80,1,26,358,340)], '000123.jpg'), ([(89,89,89,75,101,358,302)], '000556.jpg'), ([(68,68,54,3,93,383,273)], '000712.jpg'), ([(94,77,58,150,120,443,183)], '000270.jpg'), ([(55,55,55,47,93,436,254)], '000281.jpg'), ([(135,152,173,3,2,500,334)], '000312.jpg'), ([(121,111,98,1,39,367,270)], '000333.jpg'), ([(102,113,74,38,36,325,426)], '000450.jpg'), ([(72,55,78,2,39,498,347)], '000689.jpg'), ([(104,108,116,85,36,447,225)], '000774.jpg')]
res=[]
for i in range(10):
	nm=temp[i][1]
	t=temp[i][0]
	d=0
	for j in range(len(img)):
		for k in range(7):
			d+=abs(img[j][k]-t[j][k])
	res.append((d,nm))
res=sorted(res)
for i in range(10):
	img_nm=res[i][1]
	img=cv2.imread(r'G:\tftest\tf-faster-rcnn-master\tf-faster-rcnn\tf-faster-rcnn\data\VOCdevkit2007\VOC2007\JPEGImages\\'+img_nm)
	cv2.imwrite(r"G:\tftest\tf-faster-rcnn-master\tf-faster-rcnn\tf-faster-rcnn\data\VOCdevkit2007\VOC2007\results\000556\000556_0\\"+str(i)+'_'+img_nm,img)
	cv2.waitKey()