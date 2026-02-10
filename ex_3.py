import matplotlib.pyplot as plt

img1 = input('Enter Input Image File Name=')

data1 = plt.imread(img1)
shape1 = data1.shape
r, c, d = shape1[0], shape1[1], shape1[2]
print('r=', r, ' c=', c, ' d=', d)

data2 = data1[0:r//2, :, :]   # upper half

# to display 2 images (original + upper half)
rows = 1
columns = 2
fig = plt.figure(figsize=(50,50))

# To display original image
fig.add_subplot(rows, columns, 1)
plt.imshow(data1)
plt.axis('off')
plt.title('Original Image')

# To display upper half of image
fig.add_subplot(rows, columns, 2)
plt.imshow(data2)
plt.axis('off')
plt.title('Upper Half of Image1')

plt.show()
