import requests # HTTP library

from plotly.graph_objs import Bar

from plotly import offline

# # Make an API call and store the response.

# store URL to send PAI call to variabnle
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# API call header dictionary/json 
headers = {'Accept': 'application/vnd.github.v3+json'}

# send api call with headers, store response to t
r = requests.get(url, headers=headers)

# display status code of API call
print(f"Status code: {r.status_code}")

# # Process results.

response_dict = r.json()# JSONify r, and store to response_dict

# assign json_object->items to repo_dicts variable
repo_dicts = response_dict['items']

# lists to store links, stars, and labels
repo_links, stars, labels = [], [], []

# traverse through each item/dictionary in repo_dicts
for repo_dict in repo_dicts:

    repo_name = repo_dict['name'] # set name

    repo_url = repo_dict['html_url'] # set URL

    # set html anchor tag with URL
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"

    repo_links.append(repo_link) # set link

    # append value to stars list
    stars.append(repo_dict['stargazers_count'])

     # set owner login
    owner = repo_dict['owner']['login']

    # set description
    description = repo_dict['description']

    # set label
    label = f"{owner}<br />{description}"

    labels.append(label) # append label to list of labels


# # Make visualization.

# data parameter to pass to plot
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    }, # end marker
    'opacity': 0.6,
}] # end data

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }, # end xaxis
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }, # end yaxis

} # end my_layout

# create dictionary with plot parameters
fig = {'data': data, 'layout': my_layout}

# set plot using parameters and store to python_repos.html
offline.plot(fig, filename='python_repos.html')
