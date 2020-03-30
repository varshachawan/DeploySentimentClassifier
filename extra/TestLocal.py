import http.client

conn = http.client.HTTPConnection("0.0.0.0:5000")

payload = "{\n\t\"text\": \"Hi Bhusha\"\n}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/predict?=", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))