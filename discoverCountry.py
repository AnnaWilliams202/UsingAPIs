import requests

country = input("Enter a country name: ")
url = f'https://restcountries.com/v3.1/name/{country}'

response = requests.get(url)
data = response.json()

info  = data[0]
name = info['name']['common']
capital = info['capital']
region = info['region']
population = info['population']
languages = ', '.join(info['languages'].values())


print(f'Capital: {capital}')
print(f'Region: {region}')
print(f'Population: {population}')
print(f'Languages: {languages}')

