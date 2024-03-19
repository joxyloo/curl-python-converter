
import requests

response = requests.post("https://example.com/api/data",
    data='{"key1": "value1", "key2": "value2"}',
    headers={
        "Authorization": "Bearer YOUR_TOKEN_HERE",
        "Content-Type": "application/json"
    },
    cookies={},
    auth=(),
)

if response.status_code == 200:
    print(response.content)
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
