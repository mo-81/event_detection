import pymongo

from pymongo import MongoClient

db = MongoClient('mongodb://panruijie:panruijie314@121.48.165.123:30011')['tweet_stream']['test_3_22_true']

keywords=[]

for item in db.find({},{"geo":1,"timestamp_ms":1,"words":1}).batch_size(2000).limit(100):
    print(item)
    bag_words = item['words']
    print(bag_words)
    for word in bag_words:
        keywords.append(word['word'])
    print(keywords)
    break;