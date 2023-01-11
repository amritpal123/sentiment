

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



def volumeChart(df_dic):
    

    
    x=tuple(df_dic.keys())
    y=tuple(df_dic.values())



    plt.barh(x,y,color='blue')
    
    plt.title('Total Tweets')
    plt.xlabel('No. of Tweets')
    plt.ylabel('Topics')

    plt.savefig("D:/tweetweb/tweetweb/sentiment/static/image/vol.png",bbox_inches='tight')

    plt.close()

    
    return True

