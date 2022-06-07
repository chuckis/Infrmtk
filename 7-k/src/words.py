# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


text_file = ''.join(open('/home/ishchuk/hhgttg.txt'))
stopwords = set(STOPWORDS)


wordcloud = WordCloud(width = 800, height = 600,
				background_color ='white',
				stopwords = stopwords,
				min_font_size = 10).generate(text_file
            )

# plot the WordCloud image					
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
