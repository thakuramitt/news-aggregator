from newsapi import NewsApiClient

from django.db import IntegrityError


from news.uuids.generateID import generateUUIDfromString 

from .models import NewsArticle

newsapi = NewsApiClient(api_key='044d9f64aa3144fd88b1bdc965218675')


# def fetchingFunc(query):

#     all_articles = newsapi.get_everything(q=query, language='en')

#     list =  all_articles.get('articles', [])

#     for article in list:

#         hashId = generateID.generateUUIDfromString(article['title']),

#         uuidfromDB = NewsArticle.objects.values_list("uuid")
        
#         with open('uuids-list.txt', 'w', newline='') as uuidFile:
            
#             writer = csv.writer(uuidFile)
            
#             writer.writerows(uuidfromDB)

#         if article['title'] != "[Removed]" :

#             with open('uuids-list.txt', 'r') as uuidFile:

#                 if not(hashId in uuidFile):
                
#                     NewsArticle.objects.create(
#                         genre = query,
#                         uuid = hashId,
#                         title=article['title'],
#                         author=article['author'],
#                         description=article['description'],
#                         url=article['url'],
#                         publishedAt=article['publishedAt'],
#                         urlToImage = article['urlToImage'],
            
#                 )
#                 else:
#                     pass


#     return all_articles




# def fecthingfuncTo(query):


#     all_articles = newsapi.get_everything(q=query, language='en')

#     list =  all_articles.get('articles', [])

#     for article in list:

#         hashId = generateID.generateUUIDfromString(article['title']),

#         if article['title'] != "[Removed]" and  not (NewsArticle.objects.filter(uuid = hashId).exists()):
            
#             NewsArticle.objects.create(
#                 genre = query,
#                 uuid = hashId,
#                 title=article['title'],
#                 author=article['author'],
#                 description=article['description'],
#                 url=article['url'],
#                 publishedAt=article['publishedAt'],
#                 urlToImage = article['urlToImage'],
            
#             )

#     return all_articles



def fecthingfuncToo(query):

    all_articles = newsapi.get_everything(q=query, language='en')

    articleList =  all_articles.get('articles', [])

    uuidList = list(NewsArticle.objects.values_list("uuid", flat=True))

    #print(uuidList)


    for article in articleList:

        # uuidDatabase = pd.DataFrame({"title":NewsArticle.objects.values_list("title"),"uuid":NewsArticle.objects.values_list("uuid")})

        # print(uuidfromDatabase.keys)
        # print(uuidfromDatabase.values)

        # uuidFromDatabase = uuidDatabase.to_dict()

        hashId = generateUUIDfromString(article['title'])

        #print(hashId)

        #print(article)

        if (article['title'] != "[Removed]") and (hashId not in uuidList):
            
            try:
                NewsArticle.objects.create(
                    genre = query,
                    uuid = hashId,
                    title=article['title'],
                    author=article['author'],
                    description=article['description'],
                    url=article['url'],
                    publishedAt=article['publishedAt'],
                    urlToImage = article['urlToImage'],
                
                )
            except IntegrityError:
                print(article['title'])
    return all_articles



