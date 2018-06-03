from PIL import Image

myImage1 = Image.open("wing_zero.jpg")
myImage1.show()
print(myImage1.size)
#OUTPUT: (1280, 720)

myImage2 = Image.open("endless_waltz.jpg")
print(myImage2.size)
#OUTPUT: (1440, 1080)

size = 200, 200
myImage2.thumbnail(size)
myImage2.show()
print(myImage2.size)
#OUTPUT: (200, 150)

myImage_copy = myImage1.copy()

image_position = (25, 25)

myImage_copy.paste(myImage2, image_position)
size_1 = 900, 900
myImage_copy.thumbnail(size_1)
myImage_copy.show()

#Check out the file image_processing_5.png for the output.
