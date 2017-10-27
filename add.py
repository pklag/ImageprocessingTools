import cv2
import os
#changgge
tiflist = []
Commonpath = str(os.path.dirname(os.path.abspath(__file__)))

filelist = os.listdir(Commonpath)



for i in range(len(filelist)):
	if filelist[i][-4:] == "tiff" or filelist[i][-3:] == "tif":
		tiflist.append(filelist[i])

print "Amount of .tiff" + str(len(tiflist))

img1 = cv2.imread(tiflist[0],cv2.IMREAD_UNCHANGED)
#print "Value of pixel[306][628]:   " + str(img1[306][628])
img2 = cv2.imread(tiflist[1],cv2.IMREAD_UNCHANGED)
#print "Value of pixel[306][628]:   " + str(img2[306][628])

img1 = cv2.addWeighted(img1,1./(len(tiflist)),img2,1./(len(tiflist)),0.)#/(len(tiflist))
for i in range(2,len(tiflist)):
	img2 = cv2.imread(tiflist[i],cv2.IMREAD_UNCHANGED)
#	print "Value of pixel[306][628]:   " + str(img2[306][628])
	img1 = cv2.addWeighted(img1,1.,img2,1./(len(tiflist)),0.)

resized = cv2.resize(img1,None,fx=.3, fy=.3, interpolation = cv2.INTER_CUBIC)
cv2.imshow('dst',resized)

#print "Average of pixel[306][628]: " + str(img1[306][628])

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(Commonpath + '/result/Skript.tiff',img1)