#https://shanikaperera11.medium.com/positive-or-negative-spam-or-not-spam-a-simple-text-classification-problem-using-python-727efd64c238
#https://towardsdatascience.com/a-beginners-guide-to-sentiment-analysis-in-python-95e354ea84f6

import nltk.classify.util
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_most_used_word_cloud(filename,data):
    #textt = " ".join(review for review in data["Review"])
    review_str=""
    for entry in data["Review"]:
        if (type(entry)==str):
            review_str+=entry

    wordcloud = WordCloud().generate(review_str)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(filename)
    plt.show()


