import requests

city = input('Enter city name: ')

url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

print(res.text)