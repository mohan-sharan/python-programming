from PIL import Image, ImageOps

myImage = Image.open("kid_goku.jpg")

print(myImage.mode)

#OUTPUT: RGB

myImage.show()

inverted_image = ImageOps.invert(myImage)
inverted_image.show()

gray_scale = ImageOps.grayscale(myImage)
gray_scale.show()

mirror_image = ImageOps.mirror(myImage)
mirror_image.show()

flipped_image = ImageOps.flip(myImage)
flipped_image.show()