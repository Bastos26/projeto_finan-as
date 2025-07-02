import requests
import json
token="tncDfegoH942k84xhJdiMf"
ativo=input('digite um ativo:')
url = f'https://brapi.dev/api/quote/{ativo}?token={token}'
response=requests.get(url)
data=response.json()
print(json.dumps(data, indent=4, ensure_ascii=False))

