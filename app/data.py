from newsapi import NewsApiClient
import pandas as pd

def getData():
    # Init
    newsapi = NewsApiClient(api_key='f94eb9b34e044d5db9cb4103df67046e')

    articles = newsapi.get_everything(q='',
                                          sources='the-verge',
                                          domains='https://www.theverge.com/',
                                          language='en',
                                     )
    
    df = pd.DataFrame (articles["articles"])
    df = df.dropna()
    df = df.drop(['source', 'author','description','urlToImage','content'], axis=1)

    for i, row in df.iterrows():
        title = row['title']
        url = row['url']
        row['url']='<a href="'+url+'">'+title+"</a>"
        row['publishedAt']= row['publishedAt'].replace("T"," ")
        row['publishedAt']= row['publishedAt'].replace("Z"," ")

    df = df.drop(['title'], axis=1)
    df.rename(columns = {'url':'Headline', 'publishedAt' : 'Published time'}, inplace = True)

    return df