import requests

month = input("Enter a month: ")
day = input("Enter a day: ")

url = f'https://history.muffinlabs.com/date/{month}/{day}'
response = requests.get(url)
data = response.json()

events = data['data']['Events']

for event in events:
    print(f'Year: {event["year"]}')
    print(f'Event: {event["text"]}')
    print(f'Link: {event["links"][0]["link"]}')
    print('\n')

