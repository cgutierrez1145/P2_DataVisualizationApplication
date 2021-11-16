from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die # import Die class from die.py

# get num_sides of dice from user
user_num_sides = int(input("Enter the number of sides of the die: "))

# get number of tests to execute from user
user_num_tests = int(input("How many times should the dice be rolled? "))

# Create a D12.
my_die = Die(user_num_sides)

results = [] # Roll die, store results in a list as int from 1-user_num_sides.

for roll_num in range(user_num_tests): # execute loop user_num_tests times
    result = my_die.roll() # randomly return value from 1-user_num_sides
    # append value (1-user_num_sides) as int to results array
    results.append(result)
    
# Analyze the results.
frequencies = [] # number of times a specific value occurs

# increment over values from 1-user_num_sides (last value user_num_sides+1 is excluded)
for value in range(1, my_die.num_sides+1): 
     # count occurences of value in results
    frequencies.append(results.count(value)) 
    
# # Visualize the results.
# create a list from 1-user_num_sides
x_values = list(range(1, my_die.num_sides+1))

# Create Bar Chart:
  # X-Axis range is 1 - num_sides
  # Y-Axis range is all frequencies in range from 0 to number of tests
data = [Bar(x=x_values, y=frequencies)] 

x_axis_config = {'title': 'Result of Roll'} # title of X- Axis

y_axis_config = {'title': 'Frequency of Result'} # Title of Y Axis

# Chart main title 
my_layout = Layout(title='Results of rolling one D' + str(user_num_sides) + ' ' + str(user_num_tests) + ' times',
        xaxis=x_axis_config, yaxis=y_axis_config) # add X and Y axis titles to Chart

# plot chart with given parameters
offline.plot({'data': data, 'layout': my_layout}, filename='d' + str(user_num_sides) + '_' + str(user_num_tests) + 'executions.html')
