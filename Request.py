import http.client
import Handler

conn = http.client.HTTPSConnection("www.example.com")
conn.request("GET", "/")

response = conn.getresponse()
Handler.handler (response.status)

conn.close()
