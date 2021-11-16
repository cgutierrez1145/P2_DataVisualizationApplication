from operator import itemgetter

import requests # HTTP Library

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

 # assign request.Response object from URL to r
r = requests.get(url) 

# display stqatus code of HTTP connection
print(f"Status code: {r.status_code}")

# # Process information about each submission.

# JSON object representing request response data
submission_ids = r.json() 

submission_dicts = [] # list of submission in r (JSON object)

for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.

    # use f-string to parse url while inserting each sequential submission_id
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"

    r = requests.get(url) # access new URL ass ign return object to r

    # display stqatus code of HTTP connection
    print(f"id: {submission_id}\tstatus: {r.status_code}")

    response_dict = r.json() # assign request.Response object from URL to r
    
    # Build a dictionary for each article.
    submission_dict = {

        'title': response_dict['title'],

        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",

        'comments': response_dict['descendants'],
    }

    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:

    print(f"\nTitle: {submission_dict['title']}")

    print(f"Discussion link: {submission_dict['hn_link']}")

    print(f"Comments: {submission_dict['comments']}")


