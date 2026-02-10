import numpy as np
import matplotlib.pyplot as plt
img1=input("Enter your RGB Image File Name=")
img2=input("Enter your Output Image File Name=")
data1=plt.imread(img1) 
shape1=data1.shape 
r,c,d=shape1[0],shape1[1],shape1[2]
print('r=',r,' c=',c,' d=',d)
R,G,B=data1[:,:,0],data1[:,:,1],data1[:,:,2]
gray=0.2989*R+0.587*G+0.114*B 
shape2=gray.shape
r1,c1=shape2[0],shape2[1]
print('Shape2 of gray scale image=',shape2,' r1=',r1,' c1=',c1)
rows=1
columns=3

bw=gray.copy() 
for i in range(0,r1):
    for j in range(0,c1) :
        x=bw[i,j]
        if(x>=127):
            bw[i,j]=255
        else:
            bw[i,j]=0
fig=plt.figure(figsize=(30,30))
 
#To display RGB Image
fig.add_subplot(rows,columns,1)
plt.title('RGB Image')
plt.imshow(data1) 
 
#To display Gray Scale  Image
fig.add_subplot(rows,columns,2)
plt.title('Gray Scale Image')
plt.imshow(gray, cmap='gray') 
 
 
#To display B/W  Image
fig.add_subplot(rows,columns,3)
plt.title('B/W Image')
plt.imshow(bw,cmap='gray') 
plt.savefig(img2) 
plt.show()
