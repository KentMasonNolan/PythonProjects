import requests

r = requests.get('https://api.github.com/events', auth=('user', 'pass'))

r = requests.post('https://httpbin.org/post', data={'key': 'value'})

r = requests.options('https://httpbin.org/get')


print(r.status_code)
print(r.headers)
print(r.text)
print(r.url)
print(r.cookies)
print(r.elapsed)
print(r.json())
