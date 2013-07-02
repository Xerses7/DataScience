import sys
import json

def main():
    tweet_file = sys.argv[1]
    tweet_list = parse_tweets_to_dict(tweet_file)
    freq_dict = calc_frequency(tweet_list)
    print_freq_dict(freq_dict)

def print_freq_dict(freq_dict):
    for key in freq_dict:
        print "%s %f" % (key, freq_dict[key])

def calc_frequency(tweet_list):
    term_dict = {}
    term_total = 0
    for tweet_dict in tweet_list:
        if tweet_dict.has_key('delete'):
            continue
        tweet = tweet_dict['text'].split()
        term_total += len(tweet)
        for word in tweet:
            if term_dict.has_key(word):
                term_dict[word] += 1
            else:
                term_dict[word] = 1
    freq_dict = {}
    for term in term_dict:
        freq_dict[term] = float(term_dict[term])/float(term_total)
    return freq_dict

def parse_tweets_to_dict(tweet_file):
    json_tweets = []
    with open(tweet_file) as tf:
        for line in tf:
            json_tweets.append(json.loads(line, object_hook=_decode_dict))
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
