#PIL - Python Imaging Library
#A free python library for playing around with images. 
#Opening, manipulating and saving different image file formats.

from PIL import Image

myImage = Image.open("gundam_barbatos.jpg")

myImage.size

#OUTPUT:(2401, 1513)

myImage.format

#OUTPUT:'JPEG' 

myImage.show()

size = 600, 600

myImage.thumbnail(size)

myImage.show()

myImage = myImage.convert("L")

myImage.show()

#Check out the file image_processing_1.png for the output.