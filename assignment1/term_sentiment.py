import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = sys.argv[2]
    sent_dict = parse_sent_to_dictionary(sent_file)
    new_sent = find_sent(tweet_file,sent_dict)
    print_new_sent(new_sent)


def parse_sent_to_dictionary(f):
    sent_dict = {}
    f_sent = f.readlines()
    for line in f_sent:
        line_list = line.split("\t",2)
        sent_dict[line_list[0].strip("\"")] = int(line_list[1])
    return sent_dict

def find_sent(output,sent_dict):
    jsonTweets = []
    with open(output) as f:
        for line in f:
            jsonTweets.append(json.loads(line, object_hook=_decode_dict))
    new_sent_dict = {}
    for i in jsonTweets:
        if i.has_key('delete'):
            continue
        sent_count = 0
        tweet_list = i['text'].split()
        
        for w in tweet_list:
            word = w.strip("\"")
            if word == "":
                continue
            if sent_dict.has_key(word):
                sent_count += int(sent_dict[word])
            else:
                sent_count += int(0)
        
        if sent_count != 0:
            for w in tweet_list:
                word = w.strip("\"")
                if word == "":
                    continue 
                if not new_sent_dict.has_key(word) and not sent_dict.has_key(word):
                    if sent_count > 0:
                        new_sent_dict[word] = 1
                    elif sent_count < 0:
                        new_sent_dict[word] = -1
                elif new_sent_dict.has_key(word) and not sent_dict.has_key(word):
                    if sent_count > 0:
                        new_sent_dict[word] += 1
                    elif sent_count < 0:
                        new_sent_dict[word] += -1
    return new_sent_dict

def print_new_sent(new_sent):
    for key in new_sent:
        print key, float(new_sent[key])

def lines(fp):
    print str(len(fp.readlines()))

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
