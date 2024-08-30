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

x=requests.get('http://httpbin.org/get' , params={'id':'1'})
print(x.url)
x=requests.get('http://httpbin.org/get' , params={'id':'3'}, headers={'Accept':'application/json', 'test_header':'test'})
print(x.text)
x=requests.delete('http://httpbin.org/delete')
print(x.text)
x=requests.post('http://httpbin.org/post', data={'a':'b', 'c':'d', 'e':'f'})
print(x.text)
files = {'file':open('google.png', 'rb')}
x=requests.post('http://httpbin.org/post', files=files)
print(x.text)

x=requests.get('http://httpbin.org/get', auth=('username','password'))
print(x.text)
