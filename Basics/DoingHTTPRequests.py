import requests

try:
   r = requests.get('https://api.github.com/users/python', auth=('user', 'pass'))


# if r.status_code != 200:
#     print("No internet connectivity.")
# else:
#     print(r.content)
#
# r.raise_for_status()

#
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(r.url)
# print(r.cookies)
# print(r.elapsed)
# print(r.json())
