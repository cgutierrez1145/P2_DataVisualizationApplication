import csv # CSV handling library

from datetime import datetime # date and time libraries

from matplotlib import pyplot as plt

# Store file location to filename variable
filename = 'data/death_valley_2018_simple.csv'

# Open file, and store contents to variable f
with open(filename) as f:

    reader = csv.reader(f) # reader object to read contents of csv file

    header_row = next(reader) # store value of next row to variable header_row

    # # Get dates, and high and low temperatures from this file.

    # lists to store dates and high and low temperatures
    dates, highs, lows = [], [], []

    # iterate over all rows in reader
    for row in reader:

        # assign time from row[2] to variable current_date
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        # attempt to set values from row
        try:
            # cast row[4] to int and store to variable high
            high = int(row[4]) 

            # cast row[5] to int and store to variable low
            low = int(row[5])

        # execute if try block is not executed due to an exception
        except ValueError: # row[4] or row[5] were empty or NULL

            # Display error message
            print(f"Missing data for {current_date}")

        else: # executes when no exception is thrown

            dates.append(current_date) # append date to list dates

            highs.append(high) # append high to list highs

            lows.append(low) # append low to list lows

# # Plot the high and low temperatures.

plt.style.use('seaborn') # use plot style 'seaborn'

fig, ax = plt.subplots() # create layout for subplots


ax.plot(dates, highs, c='teal', alpha=0.5) # plot highs on x-axis

ax.plot(dates, lows, c='blue', alpha=0.5) # plot lows on x-axis

# fills the area between dates/highs and dates/lows
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# # Format plot.

# Set title for plot graph
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"

ax.set_title(title, fontsize=20) # Set font-size for graph

ax.set_xlabel('', fontsize=16) # set font size for x-axis

fig.autofmt_xdate() # rotate right and align layout

# set label for Y-Axis
ax.set_ylabel("Temperature (F)", fontsize=16)

# set appearance of ticks, tick labels, and gridlines
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show() # draw the plot graph