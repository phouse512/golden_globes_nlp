import urllib, json
import collections
import sys

# gather filename
filename = sys.argv[1]


data = []
with open(filename) as f:
    for line in f:
        data.append(json.loads(line))

# array of tweets in data[0]
for index, text in enumerate(data[0][:10]):
	print "Current Tweet %s: %s" % (index, text['text'])