import uncurl

script_content = '''
import requests

'''
curl = "curl -X POST https://example.com/api/data -H 'Content-Type: application/json' -H 'Authorization: Bearer YOUR_TOKEN_HERE' -d '{\"key1\": \"value1\", \"key2\": \"value2\"}'"
script_content += 'response = ' + uncurl.parse(curl)

script_content += '''

if response.status_code == 200:
    print(response.content)
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
'''

# Write the content to a new script file
file_name = 'new_script.py'

with open(file_name, 'w') as file:
    file.write(script_content)

print(f"Script '{file_name}' created successfully!")

