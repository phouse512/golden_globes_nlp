import urllib, json
import collections
import sys

# gather filename
filename = sys.argv[1]


data = []
with open(filename) as f:
    for line in f:
        data.append(json.loads(line))

frequency_map = {}
# array of tweets in data[0]
for index, text in enumerate(data[0]):
	print "Current Tweet %s: %s" % (index, text)
	word_array = text['text'].split(" ")
	for word in word_array:

		if frequency_map.has_key(word):
			frequency_map[word] += 1
		else:
			frequency_map[word] = 1

freq_list = sorted(frequency_map, key=frequency_map.get, reverse=True)

for i in freq_list[:100]:
	print "%s frequency: %s occurences" % (i, str(frequency_map[i]))