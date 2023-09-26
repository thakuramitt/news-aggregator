from .uuids import generateID
from . import fetching
import csv

news = fetching.fetchingFunc("bgmi-news")

uuid_news = generateID.generateUUIDfromString(news)

uuid_dictionary = {uuid_news}


print(uuid_dictionary)


# with open('uuids-list.txt', 'w', newline='') as file:
    
#     writer = csv.writer(file)

#     writer.writerow(uuid_news)

#     print(writer)









