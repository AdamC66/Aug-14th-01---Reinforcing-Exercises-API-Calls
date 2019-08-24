import requests

data = requests.get('https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json')

canada = data.json()[38]
# print (canada)

canada_hoc_url = canada['legislatures'][0]['popolo_url']

print(canada_hoc_url)

people = requests.get('https://cdn.rawgit.com/everypolitician/everypolitician-data/f7aa04dafa4e3aee1e03a3386c2653d53b7922ab/data/Canada/Commons/ep-popolo-v1.0.json').json()
one_persons_name = people['persons'][3]['given_name']
print(one_persons_name)