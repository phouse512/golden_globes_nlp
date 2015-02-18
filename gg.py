import urllib, json
import collections
import sys
from profilehooks import profile
import time
from collections import Counter
import operator

start = time.clock()

# gather filename
filename = sys.argv[1]


data = []
all_presenters = []
all_nominees = set()

def load_nominees():
	if '13' in filename:
		nominee_file = 'golden_globes_project/test2013.json'
	else:
		nominee_file = 'golden_globes_project/test2015.json'
	json_data=open(nominee_file)
	data = json.load(json_data)
	json_data.close()



	#initialize new nominee_dict
	nominee_dict = {}
	#  begin process of converting scraped json to nominee_dict that we will use
	for award in data:
		temp_dict = {}
		print award['award_name'][0]	
		for nominee in ['nominee_1', 'nominee_2', 'nominee_3', 'nominee_4', 'nominee_5']:
			try:
				new_name = award[nominee][0]
			except:
				new_name = "unknown name"
			temp_dict[new_name] = 0
			all_nominees.add(new_name)

		nominee_dict[award['award_name'][0]] = temp_dict

	#return nominee_dict to be used by award frequency
	return nominee_dict

def load_presenters(nominee_dict):
	if '13' in filename:
		presenter_file = 'golden_globes_project/presenters2013.json'
	else:
		presenter_file = 'golden_globes_project/presenter.json'
	json_data=open(presenter_file)
	presenter_data = json.load(json_data)
	json_data.close()

	presenter_dict = {}

	for element in presenter_data:
		all_presenters.append(element['presenter'])


	for award in nominee_dict:
		temp_dict = {}
		for presenter in presenter_data:
			temp_dict[presenter['presenter']] = 0
		presenter_dict[award] = temp_dict

	return presenter_dict




@profile
def load_tweets_json(filename):
	if '13' in filename:
		json_tweets=open(filename)
		data.append(json.load(json_tweets))
		json_tweets.close()
	else: 
		with open(filename) as f:
			for line in f:
				data.append(json.loads(line))

	print len(data[0])


@profile
def word_frequency(nominee_dict, presenter_dict):
	# array of tweets in data[0]
	for index, text in enumerate(data[0]):
		#if int(text['timestamp_ms']) >= 1421024400000:
		word_set = set(text['text'].split(" "))
		for this in nominee_dict:
			if set(this.split(" ")).issubset(word_set):
				for possible_presenter in presenter_dict[this]:
					if possible_presenter in text['text']:
						presenter_dict[this][possible_presenter] += 1					
				for possible_nominee in nominee_dict[this]:					
					if possible_nominee in text['text']:
						nominee_dict[this][possible_nominee] += 1

	return (nominee_dict, presenter_dict)


load_tweets_json(filename)
nominees = load_nominees()
presenters = load_presenters(nominees)
freq_list = word_frequency(nominees, presenters)
#freq_list = [nominees, presenters]
print "\n\nResults:"
print json.dumps(freq_list[0], indent=4, sort_keys=True)
print json.dumps(freq_list[1], indent=4, sort_keys=True)


final_dict = {
	"time": "90",
	"tweets": len(data[0])
} 
award_dict = {}
for award in freq_list[0]:
	winner = max(freq_list[0][award].iteritems(), key=operator.itemgetter(1))[0]
	presenters = [max(freq_list[1][award].iteritems(), key=operator.itemgetter(1))[0]]
	temp_dict = {}
	temp_dict["winner"] = winner
	temp_dict["presenters"] = presenters
	award_dict[award] = temp_dict
final_dict["awards"] = award_dict

with open('final.json', 'wb') as fp:
    json.dump(final_dict, fp)

print final_dict


""" Produce the final json file to be used in autograder """
metadata = {}

if '13' in filename:
	metadata['year'] = 2013
else:
	metadata['year'] = 2015

hosts = {}
hosts['method'] = 'hardcoded'
hosts['method_description'] = 'Since the presenters were announced early, we just hardcoded these into our system.'
nominees_dict = {}
nominees_dict['method'] = 'scraped'
nominees_dict['method_description'] = 'We used the goldenglobes.com website to scrape the nominees using a python library called "scrapy" that allowed us to output nominees to a json file our program uses'
awards_dict = {}
awards_dict['method'] = 'scraped'
awards_dict['method_description'] = 'As mentioned previously, we scraped from goldenglobes.com in similar fashion to get the awards along with nominees. Some editing was needed to clean up names.'
presenters_dict = {}
presenters_dict['method'] = 'scraped'
presenters_dict['method_description'] = 'Scraped using the same scraper as above.  Some more cleaning was needed in this area however'
metadata['names'] = { 'hosts': hosts, 'nominees': nominees_dict, 'awards': awards_dict, 'presenters': presenters_dict }
nominee_mapping = {
	'method': 'scraped',
	'method_description': 'As we scraped the nominees as previously mentioned, we also grabbed their association to the awards from the div header'
}
presenter_mapping = {
	'method': 'detected',
	'method_description': 'We had one list of all the presenters that we then did our best to detect from.'
}
metadata['mappings'] = { 'nominees': nominee_mapping, 'presenters': presenter_mapping }

print json.dumps(metadata, indent=4, sort_keys=True)

hosts = ['Tina Fey', 'Amy Poehler']
winners = []
awards = []
for award in final_dict['awards']:
	winners.append(final_dict['awards'][award]['winner'])
	awards.append(award)

data_dict = {}
data_dict['unstructured'] = { 'hosts': hosts, 'winners': winners, 'awards': awards, 'presenters': all_presenters, 'nominees': list(all_nominees) }
data_dict['structured'] = {}
for award in final_dict['awards']:
	temp_dict = {}
	award_nominees = []
	save_index = 0
	temp_dict['presenters'] = final_dict['awards'][award]['presenters']
	temp_dict['winner'] = final_dict['awards'][award]['winner']
	for nominees_temp in nominees[award]:
		award_nominees.append(nominees_temp)
	temp_dict['nominees'] = award_nominees
	data_dict['structured'][award] = temp_dict


print json.dumps(data_dict, indent=4, sort_keys=True)

autograder_dict = { 'metadata': metadata, 'data': data_dict}

with open('to_be_graded.json', 'wb') as fp:
    json.dump(autograder_dict, fp)

