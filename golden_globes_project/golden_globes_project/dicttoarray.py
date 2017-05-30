import json

json_tweets=open('../presenter.json')
data = (json.load(json_tweets))
json_tweets.close()

json_tweet=open('../test2015.json')
awards = (json.load(json_tweet))
json_tweets.close()

presenter_array = []
for presenter in data:
	presenter_array.append(presenter['presenter'])

final = {}
for award in awards:
	final[award['award_name'][0]] = presenter_array




with open('final_presenters2015.json', 'wb') as fp:
    json.dump(final, fp)