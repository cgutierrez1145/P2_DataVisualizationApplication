import json

# Explore the structure of the data.
filename = './global_data/data/eq_data_1_day_m1.json'
with open(filename) as f: # open file 
    all_eq_data = json.load(f) # convert returned data to json object

# access key features from json object and assign it to variable
all_eq_dicts = all_eq_data['features']

# magnitude, latitude, and longitude of earthquake
mags, lons, lats = [], [], []

# go through each dictionary in all_dictionaries
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # assign mag value

     # assign longitude value from json_object->geometry->coordinates->[0]
    lon = eq_dict['geometry']['coordinates'][0]

    # assign latitude value from json_object->geometry->coordinates->[1]
    lat = eq_dict['geometry']['coordinates'][1]

    mags.append(mag) # append magnitude to list of magnitudes

    lons.append(lon) # append longitude to list of longitudes

    lats.append(lat) # append latitudes to list of latitudes

print(mags[:10]) # print the first ten magnitudes 

print(lons[:5]) # print the first 5 longitudes

print(lats[:5]) # print the first 5 latitudes
