from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
file_name = input("Please enter the name of the text file ie 'filename.txt': ")
text = open(path.join(d, file_name)).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
#alice_mask = np.array(Image.open(path.join(d, "heart.jpg")))
image_shape = input("Enter the name of your image ie 'pic.jpg': ")
mask = np.array(Image.open(path.join(d, image_shape)))

stopwords = set(STOPWORDS)
stopwords.update(('django girls','friendly', 'workshop','open','twitter'))

# define our method
chosen_color = input("Please choose a background color: black, white, red etc :")
wc = WordCloud(background_color=chosen_color, max_words=2000, mask=mask, stopwords=stopwords)
# generate word cloud
wc.generate(text)

# store to file
new_file_name = input("what do you want to name your file? ie: 'cool_pic.jpg': ")
wc.to_file(path.join(d, new_file_name))

# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(mask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
