from PIL import Image, ImageDraw, ImageFont

myImage = Image.open("vegito.png").convert('RGBA')
size = 800, 800
myImage.thumbnail(size)
myImage.show()

#Create a transparent text color image for the text
myText = Image.new('RGBA', myImage.size, (255,255,255,0))

#Accessing font types
fnt1 = ImageFont.truetype('Pillow/Tests/fonts/DejaVuSans.ttf', 35)
fnt2 = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 30)

d = ImageDraw.Draw(myText)

#Draw the text
d.text((665,400), "Vegito", font=fnt1, fill=(255,255,255))
#White Color: (R,G,B) - (255,255,255)
d.text((10,10), "End Of The World Blast", font=fnt2, fill=(0,0,0))
#Black color: (R,G,B) - (0,0,0)

outputImage = Image.alpha_composite(myImage, myText)
outputImage.show()

#Check out the file image_processing_6.png for the output.
