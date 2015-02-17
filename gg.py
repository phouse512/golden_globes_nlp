import urllib, json
import collections
import sys
from profilehooks import profile
import time
from collections import Counter

start = time.clock()

# gather filename
filename = sys.argv[1]


data = []

def load_nominees():
	json_data=open('golden_globes_nominees/test.json')
	data = json.load(json_data)
	json_data.close()

	#initialize new nominee_dict
	nominee_dict = {}
	#  begin process of converting scraped json to nominee_dict that we will use
	for award in data:
		temp_dict = {}
		for nominee in ['nominee_1', 'nominee_2', 'nominee_3', 'nominee_4', 'nominee_5']:
			new_name = award[nominee][0]
			temp_dict[new_name] = 0
		print award['award_name'][0]
		nominee_dict[award['award_name'][0]] = temp_dict

	#return nominee_dict to be used by award frequency
	return nominee_dict

@profile
def load_tweets_json():
	with open(filename) as f:
	    for line in f:
	        data.append(json.loads(line))


@profile
def word_frequency(nominee_dict):
	# array of tweets in data[0]
	for index, text in enumerate(data[0]):
		if int(text['timestamp_ms']) >= 1421024400000:
			word_set = set(text['text'].split(" "))
			for this in nominee_dict:
				if set(this.split(" ")).issubset(word_set):					
					for possible_nominee in nominee_dict[this]:					
						if possible_nominee in text['text']:
							nominee_dict[this][possible_nominee] += 1

	return nominee_dict


load_tweets_json()
nominees = load_nominees()
print json.dumps(nominees, indent=4, sort_keys=True)
freq_list = word_frequency(nominees)
print "\n\n"
print json.dumps(freq_list, indent=4, sort_keys=True)