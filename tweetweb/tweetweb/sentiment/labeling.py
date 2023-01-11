# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:27:16 2020

@author: aarus
"""



from textblob import TextBlob

import pandas as pd




def sentiMent(dataset):

    
    for i in range(0,len(dataset)):
        
        analysis=TextBlob(dataset['Tweet'][i])
        
        if analysis.polarity==0:
            l='Neutral'
        
        elif analysis.polarity > 0:
            if analysis.polarity<0.5:
                l='Weakly Positive'
            else:
                l='Highly Positive'
        elif analysis.polarity < 0 :
            if analysis.polarity>-0.5:
                l='Highly Negative'
            else:
                l='Weakly Negative'
        
            
         
        dataset['Label'][i]=l
       
        
    return dataset
        
        

