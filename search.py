import cv2
#image_name			object_class_code						color_code					words
#[(0, '000456.jpg'), (0, '000536.jpg'), (0, '000782.jpg'), (1, '000054.jpg'), (1, '000207.jpg'), (1, '000231.jpg'), (1, '000479.jpg'), (1, '000512.jpg'), (1, '000534.jpg'), (1, '002229.jpg')]
#[(110,117,113,92,43,425,303)] [(35,49,66,121,117,174,160)] [(156,159,158,142,255,199,296)]
#[(74,74,67,11,90,481,330)] [(117,116,120,463,207,498,320)] [(92,96,94,102,174,211,223)]
#[(106,105,93,1,165,330,497)] [(41,39,47,95,361,139,422)] [(77,88,110,161,321,296,420)]
#[(100,93,94,24,54,472,292)]							 [(122,130,137,40,61,183,108)]
#[(54,40,31,1,205,113,320)] 								[(67,73,76,188,124,334,347)]
#[(55,36,22,87,110,278,206)] [(46,32,18,337,124,366,227)]
#							[(180,144,133,34,2,374,500)] [(204,198,192,15,305,131,351)]
#[(117,118,114,20,79,423,357)] 								[(224,220,219,90,321,151,342)]
#							[(106,64,61,3,15,463,500)] [(66,53,46,163,188,300,242)]
#[(120,121,120,37,95,433,304)] [(87,85,88,385,188,425,280)]
db=open('res.txt','r')
lines=db.readlines()
search_image="(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2)"
search_image=search_image[1:-1].split(',')
temp=[]
for line in lines:
	line=line.strip().split('\t')
	occ_t=line[1]
	nm=line[0]
	occ_t=occ_t[1:-1].split(',')
	s=0
	for i in range(len(occ_t)):
		s+=abs(int(occ_t[i])-int(search_image[i]))
	temp.append((s,nm))
res=sorted(temp)
print(res[:10])
for i in range(10):
	img_nm=res[i][1]
	img=cv2.imread(r'G:\tftest\tf-faster-rcnn-master\tf-faster-rcnn\tf-faster-rcnn\data\VOCdevkit2007\VOC2007\JPEGImages\\'+img_nm)
	cv2.imwrite(r"G:\tftest\tf-faster-rcnn-master\tf-faster-rcnn\tf-faster-rcnn\data\VOCdevkit2007\VOC2007\results\000556\000556_1\\"+str(i)+'_'+img_nm,img)
	cv2.waitKey()