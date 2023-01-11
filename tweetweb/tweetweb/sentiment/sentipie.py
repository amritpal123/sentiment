# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:02:38 2020

@author: aarus
"""

import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def sentiFig(dataset):
    sentiment=dataset['Label'].value_counts()
    print(sentiment)
    total=0
    size=[]
    
    for i in sentiment.values:
        total+=i
        size.append(i)
    
    
    
    
    explode =[]
    for i in range(len(sentiment)):
        explode.append(0.05)
        
    explode=tuple(explode)
    
    
    #correct this labels=['Positive '+str(round((pos/total)*100,2))+'%','Neutral '+str(round((neutral/total)*100,2))+'%','Negative '+str(round((neg/total)*100,2))+'%']
    
    
    l2=sentiment.keys()
    #fig=plt.figure()
    patches, texts=plt.pie(size,labels=l2,shadow=True,explode=explode)
    
    
    plt.legend(patches,l2,loc='best') #plt.legend(patches,lables,loc='best')
    
    plt.title("Sentimental Analysis on "+ str(total)+ " Tweets")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig("D:/tweetweb/tweetweb/sentiment/static/image/senti.png",bbox_inches='tight')


    plt.close()
    
    return True

