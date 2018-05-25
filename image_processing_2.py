from PIL import Image

import ImageFilter

myImage = Image.open("gundam_barbatos.jpg")
size = 800, 800
myImage.thumbnail(size)
myImage.show()

myImage1 = myImage.filter(ImageFilter.BLUR)
myImage1.show()

myImage2 = myImage.filter(ImageFilter.MinFilter(3))
myImage2.show()

myImage3 = myImage.filter(ImageFilter.MaxFilter(3))
myImage3.show()

myImage4 = myImage.rotate(45)
myImage4.show()

myImage5 = myImage.rotate(90)
myImage5.show()

flipped_image = myImage.transpose(Image.FLIP_LEFT_RIGHT)
flipped_image.show()
