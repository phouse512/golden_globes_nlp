import urllib, json
import collections
import sys
import nltk
import pickle

def topNames(name, num):
	b = {}
	for jName in name:
		if len(name[jName][num]) < 3:
			top_three = name[jName][num]
		else:
			fdist = nltk.FreqDist(name[jName][num]) 
			most_common = fdist.max()   
			top_three = fdist.keys()[:3] 
		if (name[jName][0]+name[jName][1] > 50 or jName == "Margaret Cho"):
			b[jName] = [(name[jName][0])/(name[jName][0]+name[jName][1]+1),name[jName][2],top_three]
	return b

def getCelebSentiment(tweetJSON):

	nameFile = open("words/celebs.txt", 'r')
	nameDob = [line.split('\n') for line in nameFile.readlines()]
	names = [line[0] for line in nameDob]
	name = dict((nameIn,[0,0,0,[],[]]) for nameIn in names)

	posFile = open("words/positiveWords.txt", 'r')
	posDob = [line.split('\n') for line in posFile.readlines()]
	posWords = [line[0] for line in posDob]

	negFile = open("words/negativeWords.txt", 'r')
	negDob = [line.split('\n') for line in negFile.readlines()]
	negWords = [line[0] for line in negDob]

	funFile = open("words/funnyWords.txt", 'r')
	funDob = [line.split('\n') for line in funFile.readlines()]
	funWords = [line[0] for line in funDob]

	json_data=open(tweetJSON)
	data = json.load(json_data)

	for i in range(0,len(data),50):
		tokens = nltk.word_tokenize(data[i]["text"])
		for iName in name:
			jName = iName.split(" ")[1]
			if (jName in tokens) and ("RT" not in tokens):
				for p in posWords:
					if p in tokens:
						name[iName][0] = name[iName][0] + 1.0
						name[iName][3].append(p) 
				for n in negWords:
					if n in tokens:
						name[iName][1] = name[iName][1] + 1.0
						name[iName][4].append(n) 
				for f in funWords:
					if f in tokens:
						name[iName][2] = name[iName][2] + 1
	popular = topNames(name,3)
	unpopular = topNames(name,4)

	mostpopular = sorted(popular.items(), key=lambda x: x[1], reverse = True)
	mostpopular =  mostpopular[:5]
	leastpopular = sorted(unpopular.items(), key=lambda x: x[1])
	leastpopular = leastpopular[:5]
	'''
	#JSON file with tags
	for ii in mostpopular:
		dic = {'popPercent': ii[1][0], 'humorCount': ii[1][1], 'Sentiment': ii[1][2]}
		mp[ii[0]]= dic
	'''
	mp = {}
	for ii in mostpopular:
		mp[ii[0]] = [ii[1][0],ii[1][1],ii[1][2]]
	lp = {}
	for ii in leastpopular:
		lp[ii[0]] = [ii[1][0],ii[1][1],ii[1][2]]

	#mostfunny = sorted(b.items(), key=lambda x: x[1][1], reverse = True)
	#print mostfunny
	with open('data_fun/dataPop.json', 'w') as outfile:
		json.dump(mp, outfile)
	with open('data_fun/dataUnpop.json', 'w') as outfile:
		json.dump(lp, outfile)

def main():
	getCelebSentiment(sys.argv[1])

main()


