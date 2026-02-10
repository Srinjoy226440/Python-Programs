#image_processing_1.py: Write a program to display an image on Screen 
import matplotlib.pyplot as plt
import numpy as np
file1=input("Enter Image File Name=") # Reading Image File  Name
data1 = plt.imread(file1) # Extracting pixels data from Image file
plt.imshow(data1) # Reconstruting  pixels to image
shape1=data1.shape
r,c,d=shape1[0],shape1[1],shape1[2]
print("r=",r," c=",c," d=",d)
plt.savefig("output1.jpg")
plt.show()
