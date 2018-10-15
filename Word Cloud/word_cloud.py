import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud

textFile1 = open("some_text_1.txt", "r").read()
wordcloud1 = WordCloud().generate(textFile1)
plt.imshow(wordcloud1, interpolation="bilinear")
plt.axis("off")
plt.show()

textFile2 = open("some_text_2.txt", "r").read()
#lower - max_font_size
wordcloud2 = WordCloud(max_font_size=38).generate(textFile2)
plt.imshow(wordcloud2, interpolation="bilinear")
plt.axis("off")
plt.show()

gundam_image = Image.open("GN00.jpg")
gundam_image_mask = np.array(gundam_image)
wordcloud3 = WordCloud(mask=gundam_image_mask).generate(textFile2) 
plt.imshow(wordcloud3, interpolation="bilinear")
plt.axis("off")
plt.show()

#References 
#http://gundam.wikia.com/wiki/GN-0000%2BGNR-010_00_Raiser
#http://dc.wikia.com/wiki/Batman_Beyond_(TV_Series)
#https://www.datacamp.com/community/tutorials/wordcloud-python