import requests # HTTP Library

import json

# # Make an API call, and store the response.

# store the value of the URL to send API call to url variable
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'

r = requests.get(url) # Send API call to URL, and store response to r

# Display status code of API call (HTTP Connection)
print(f"Status code: {r.status_code}")

# # Explore the structure of the data.

response_dict = r.json() # set HTTP response to JSON object

# store file location to readable_file variable
readable_file = 'data/readable_hn_data.json'

# Open file for writing fron beginning of file
with open(readable_file, 'w') as f:
    # store JSON object to file, with indent of 4 for readability
    json.dump(response_dict, f, indent=4)
