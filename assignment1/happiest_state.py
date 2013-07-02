import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = sys.argv[2]
    sent_dict = parse_sent_to_dictionary(sent_file)
    tweet_list = parse_tweets_to_dict(tweet_file)
    us_tweets = get_us_tweets(tweet_list)
    sent_state_dict = calc_sent(us_tweets,sent_dict)
    happiest = calc_happiest(sent_state_dict)
    print happiest
    
def calc_happiest(sent_state_dict):
    happiness = {}
    for state in sent_state_dict:
        if happiness.has_key(state):
            happiness[state] += float(sent_state_dict[state])
        else:
            happiness[state] = float(sent_state_dict[state])
    max_val = 0
    happiest = ""
    for key in happiness:
        if happiness[key] > max_val:
            max_val = happiness[key]
            happiest = key
    return happiest
     

def get_us_tweets(tweet_list):
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    
    us_tweets = []

    for tweet in tweet_list:
        if tweet.has_key('delete'):
            continue
        user = tweet['user']
        location = user['location'] or ""
        if location[-2:] in states:
            us_tweets.append(tweet)
    return us_tweets

def parse_sent_to_dictionary(f):
    sent_dict = {}
    f_sent = f.readlines()
    for line in f_sent:
        line_list = line.split("\t",2)
        sent_dict[line_list[0]] = int(line_list[1])
    return sent_dict

def calc_sent(tweets,sent_dict):
    sent_state_dict = {}
    for i in tweets:
        if i.has_key('delete'):
            continue
        user = i['user']
        location = user['location']
        state = location[-2:]
        sent_count = 0
        tweet_list = i['text'].split()
        
        for word in tweet_list:
            if sent_dict.has_key(word):
                sent_count += int(sent_dict[word])
            else:
                sent_count += int(0)
        
        sent_state_dict[state] = float(sent_count)
    return sent_state_dict    

def parse_tweets_to_dict(tweet_file):
    json_tweets = []
    with open(tweet_file) as tf:
        for line in tf:
            tweet = json.loads(line, object_hook=_decode_dict)
            if tweet is None:
                continue
            else:
                json_tweets.append(tweet)
    return json_tweets

def print_loc(tweet_list):
    for tweet in tweet_list:
        user = tweet['user']
        location = user['location']
        print location   
    
    
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

    