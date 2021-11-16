import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = './global_data/data/eq_data_30_day_m1.json'

with open(filename) as f: # open file
    all_eq_data = json.load(f) # assign file return as json object

# assign json->features to variable
all_eq_dicts = all_eq_data['features'] 

# lists of magnitudes, latitudes, longitudes, and hover-texts
mags, lons, lats, hover_texts = [], [], [], []

# go through each item in all_eq_dicts
for eq_dict in all_eq_dicts:
    # magnitude = json->features->properties->mag
    mag = eq_dict['properties']['mag']

    # longitude = json->features->geometry->coordinates->[0]
    lon = eq_dict['geometry']['coordinates'][0] 

    # latitude = json->features->geometry->coordinates->[1]
    lat = eq_dict['geometry']['coordinates'][1] 

    # magnitude = json->features->properties->title
    title = eq_dict['properties']['title'] 

    mags.append(mag)  # append magnitude to list of magnitudes

    lons.append(lon) # append longitude to list of longitudes

    lats.append(lat) # append latotude to list of latitudes

    hover_texts.append(title) # append hover-text to list of hover-texts

# Map the earthquakes.
data = [{
    'type': 'scattergeo', # type of earthquakes
    'lon': lons, # longitudal coordinates of earthquakes
    'lat': lats, # latitudal coordinates of earthquakes
    'text': hover_texts, # hover-texts
    'marker': {
        'size': [5*mag for mag in mags], # get each size, multiply it by 5
        'color': mags, # color set to magnitudes
        'colorscale': 'Viridis', # coplor-scale for graph
        'reversescale': True, # scale parameter
        'colorbar': {'title': 'Magnitude'}, # set title
    },
}] # end data

my_layout = Layout(title='Global Earthquakes') # set title of map

#  draw actual map to html document
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
