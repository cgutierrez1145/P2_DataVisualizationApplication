import csv

from datetime import datetime

from matplotlib import pyplot as plt

filename = './csv/data/sitka_weather_2018_simple.csv'

# open file
with open(filename) as f:
    # assign a reader object to reader that wqill read the file
    reader = csv.reader(f) 

    header_row = next(reader) # assign next row as list to header_row

    # # Get dates, and high and low temperatures from this file.

    # dates of temperatures, high temperatures, and low temperatures
    dates, highs, lows = [], [], []

    # read file
    for row in reader:
        # create datetime object and assign it to variable
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        high = int(row[5]) # cast string val to int, asssing to variable

        low = int(row[6]) # cast string val to int, asssing to variable

        dates.append(current_date) # add current date to al dates

        highs.append(high) # add current high to list of highs

        lows.append(low) # add current low to list of lows


# # Plot the high and low temperatures.

plt.style.use('dark_background') # set style

fig, ax = plt.subplots() # create layout for subplots

# also sets color and opacity
ax.plot(dates, highs, c='magenta', alpha=0.9) # plot highs on x-axis

ax.plot(dates, lows, c='cyan', alpha=0.9) # plot lows on x-axis

# fills the area between dates/highs and dates/lows
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# # Format plot.

# Set title for plot graph
plt.title("Daily high and low temperatures - 2018", fontsize=16)

plt.xlabel('', fontsize=16) # Set font-size for plot graph

fig.autofmt_xdate() # rotate right and align layout

# set label for Y-Axis
plt.ylabel("Temperature (F)", fontsize=16)

# set appearance of ticks, tick labels, and gridlines
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show() # draw the plot graph