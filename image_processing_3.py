from PIL import Image

import ImageEnhance

myImage = Image.open("gogeta.png")
size = 700, 700
myImage.thumbnail(size)
myImage.show()

sharp = ImageEnhance.Sharpness(myImage)

sharp.enhance(4).show()
sharp.enhance(10).show()

color = ImageEnhance.Color(myImage)

color.enhance(0).show()
color.enhance(2).show()
color.enhance(4).show()

bright = ImageEnhance.Brightness(myImage)

bright.enhance(2).show()
bright.enhance(4).show()

contrast = ImageEnhance.Contrast(myImage)

contrast.enhance(2).show()
contrast.enhance(4).show()

#Check out the file image_processing_3.png for the output.