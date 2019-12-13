from django.shortcuts import render

# Create your views here.
from newsapi import NewsApiClient

# Init
def Index(request):
   newsapi = NewsApiClient(api_key='76400671e67f47fb9a8e2cd946efb07b')

# /v2/top-headlines
   topheadlines = newsapi.get_top_headlines(
                                          sources='bbc-news,the-verge'
   )
# /v2/everything
   articles = topheadlines['articles']
   desc=[]
   news=[]
   img=[]

# /v2/sources
   #sources = newsapi.get_sources()

   for i in range(len(articles)):
       myarticle=articles[i]
       news.append(myarticle['title']);
       desc.append(myarticle['description']);
       img.append(myarticle['urlToImage']);

   mylist=zip(news,desc,img);
   return render(request,'newsapp/index.html',context={"mylist":mylist})
