import requests

x = requests.get('http://httpbin.org/get')

print(x.headers)

print(x.headers['Server'])

print(x.status_code)

if x.status_code == 200:
  print("Successful!")
elif x.status_code == 404:
  print("Cannot be reached!")

print(x.elapsed)
print(x.cookies)

#x = requests.get('http://github.com', allow_redirects=False)
#print(x.headers)
#x = requests.get('http://httpbin.org/get', timeout=0.01)
#print(x.content)
x = requests.get('http://httpbin.org/cookies', cookies={'a':'b'})
print(x.content)
x = requests.Session()
x.cookies.update({'a':'b'})
print(x.get('http://httpbin.org/cookies').text)

x = requests.get('https://api.github.com/events')
print(x.json())

x = requests.get('https://www.google.com/logos/doodles/2024/paris-games-basketball-6753651837110534-la202124.gif')
with open('google2.png', 'wb') as f:
  f.write(x.content)
