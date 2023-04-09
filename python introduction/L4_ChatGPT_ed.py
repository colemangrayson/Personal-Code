"""Opening ChatGPT API"""

import requests

# Set up the API endpoint and parameters
url = 'https://api.openai.com/v1/chat/completions'
headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}
data = {
    'messages': [
        {'role': 'system', 'content': 'You: Hello'},
        {'role': 'user', 'content': 'User: How can you help me?'}
    ],
    'temperature': 0.8,
    'max_tokens': 50
}

# Make the API request
response = requests.post(url, headers=headers, json=data)

# Parse the response
if response.status_code == 200:
    result = response.json()
    completions = result['choices'][0]['message']['content']
    print('ChatGPT Response:', completions)
else:
    print('Error:', response.text)