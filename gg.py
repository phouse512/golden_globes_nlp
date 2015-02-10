import urllib, json
import collections
import sys
from profilehooks import profile
import time

start = time.clock()

# gather filename
filename = sys.argv[1]


data = []
frequency_map = {}

@profile
def load_json():
	with open(filename) as f:
	    for line in f:
	        data.append(json.loads(line))

@profile
def word_frequency():

	# array of tweets in data[0]
	for index, text in enumerate(data[0]):
		#print "Current Tweet %s: %s" % (index, text)
		word_array = text['text'].split(" ")
		for word in word_array:
			if frequency_map.has_key(word):
				frequency_map[word] += 1
			else:
				frequency_map[word] = 1

	return sorted(frequency_map, key=frequency_map.get, reverse=True)


load_json()
freq_list = word_frequency()


for i in freq_list[:100]:
	print "%s frequency: %s occurences" % (i, str(frequency_map[i]))

end = time.clock()
print "total time: %.2gs" % (end-start)