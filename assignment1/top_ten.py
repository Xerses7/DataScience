import sys
import json

def main():
    tweet_file = sys.argv[1]
    tweet_list = parse_tweets_to_dict(tweet_file)
    hashtags = parse_hashtags(tweet_list)
    print_top_ten(hashtags)

def print_top_ten(hashtags):
    count = 0
    # from StackOverflow
    # http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value
    for h in sorted(hashtags, key=hashtags.get, reverse=True):
        print h, hashtags[h]
        count += 1
        if count == 10:
            break

def parse_hashtags(tweet_list):
    hash_dict = {}
    for tweet in tweet_list:
        if tweet.has_key('entities'):
            entities = tweet['entities'] or ""
            hashtags = entities['hashtags'] or ""
            if len(hashtags) > 0:
                for term in hashtags:
                    text = term['text']                    
                    if not hash_dict.has_key(text):
                        hash_dict[text] = 1
                    elif hash_dict.has_key(text):
                        hash_dict[text] += 1
    return hash_dict

def parse_tweets_to_dict(tweet_file):
    json_tweets = []
    with open(tweet_file) as tf:
        for line in tf:
            tweet = json.loads(line, object_hook=_decode_dict)
            if tweet is None:
                continue
            elif tweet.has_key('delete'):
                continue
            else:
                json_tweets.append(tweet)
    return json_tweets

# got it from http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-unicode-ones-from-json-in-python	
def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
           key = key.encode('utf-8')
        if isinstance(value, unicode):
           value = value.encode('utf-8')
        elif isinstance(value, list):
           value = _decode_list(value)
        elif isinstance(value, dict):
           value = _decode_dict(value)
        rv[key] = value
    return rv

if __name__ == '__main__':
    main()