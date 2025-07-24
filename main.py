import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

# load the image
image = img.imread("images/input_image.jpg")
print("image shape:", image.shape)
plt.imshow(image)
plt.show()

# convert the image to grayscale
# extract the R, G, B channels using the numpy slicing
# formula to get the 2-D array without the color channels
# Gray = 0.2989 * R + 0.5870 * G + 0.1140 * B

R = image[:, :, 0]
G = image[:, :, 1]
B = image[:, :, 2]

Gray = 0.2989 * R + 0.5870 * G + 0.1140 * B

# displaying the grayscale image
plt.imshow(Gray, cmap='gray')
plt.show()
plt.imsave("results/Gray_image.jpg", Gray, cmap='gray')

# converting the grayscale into negative
# if pixel value is 255 then the negative pixel value is 0
Negative = 255 - Gray
plt.imshow(Negative, cmap='gray')
plt.show()
plt.imsave("results/negative_image.jpg", Negative, cmap='gray')

# rotating the image 90 degrees
# using numpy's rot90 function
rotated_image = np.rot90(Negative)
plt.title("90 degrees Image")
plt.imshow(rotated_image, cmap='gray')
plt.show()
plt.imsave("results/rotated_image.jpg", rotated_image, cmap='gray')

# rotating the image 180 degrees
rotated_image_180 = np.rot90(rotated_image)
plt.title("180 degrees Image")
plt.imshow(rotated_image_180, cmap='gray')
plt.show()
plt.imsave("results/rotated_image_180.jpg", rotated_image_180, cmap='gray')

# rotating the image 270 degrees
rotated_image_270 = np.rot90(rotated_image_180)
plt.title("270 degrees Image")
plt.imshow(rotated_image_270, cmap='gray')
plt.show()
plt.imsave("results/rotated_image_270.jpg", rotated_image_270, cmap='gray')

# cropping the image
crop = Gray[2000:3000, 3000:4000]  # Adjust the indices as needed
plt.imshow(crop, cmap='gray')
plt.show()
print("cropped image shape:", crop.shape)
plt.imsave("results/cropped_image.jpg", crop, cmap='gray')