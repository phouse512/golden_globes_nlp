
import json
lines = [line.strip() for line in open('presenters2013.txt')]


array = []
for line in lines:
	temp_dict= {}
	temp_dict['presenter'] = line
	array.append(temp_dict)

print array
with open('presenters2013.json', 'wb') as fp:
    json.dump(array, fp)