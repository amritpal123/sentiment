# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:26:40 2020

@author: amrit
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:50:58 2019

@author: amrit
"""

import pandas as pd

from wordcloud import WordCloud, STOPWORDS

from matplotlib import pyplot as plt


def makeWordCloud(dataset):
    
    tweets=''
    for tweet in dataset['Tweet']:
        tweet=str(tweet)
        tweet=tweet.replace('RT','')
        tweet=tweet.split(' ')
        
        for token in tweet:
            tweets+=token.lower() +' '
    
    
    stopwords = set(STOPWORDS)
    
    wordcloud=WordCloud(width=800,height=800,stopwords=stopwords,min_font_size=10).generate(tweets)
    
    plt.imshow(wordcloud)


    plt.savefig("D:/tweetweb/tweetweb/sentiment/static/image/wordc.png",bbox_inches='tight')

    plt.close()
    
    return True


