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

image_shape = input("Enter the name of your image ie 'pic.jpg': ")
mask = np.array(Image.open(path.join(d, image_shape)))

stopwords = STOPWORDS.copy()
while True:

    edit_text = input("Are there any words you don't want to show up? y/n :")

    if edit_text == 'y' or edit_text == 'Y':
        new_word = input("Write a word you don't want included: ")
        stopwords.add(new_word)
    elif edit_text == 'n' or edit_text == 'N':
        break
    else:
        break

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
