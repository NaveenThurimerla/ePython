import cgi
import http.client

server = 'www.blog.nen10.com'
url = '/'
conn = http.client.HTTPSConnection(server)
conn.request('GET', url)
response = conn.getresponse()
content_type = response.headers.get('Content-Type')
_, params = cgi.parse_header(content_type)
encoding = params.get('charset')
data = response.read()
text = data.decode(encoding)

print(f'Response returned: {response.status} ({response.reason})')
print('Body:')
print(text)