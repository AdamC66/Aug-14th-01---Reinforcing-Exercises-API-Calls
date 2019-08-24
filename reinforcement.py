import requests

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')

for item in ottawa_wards_response.json()['objects']:
    print(item['name'])