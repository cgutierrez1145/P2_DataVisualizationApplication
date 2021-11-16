import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Stor user input to variable for num_points
user_num_points = int(input(
  "\n----------------------------------------------------------------\n\n"
+ "This program generates all the steps taken during a walk in which\n" 
+ " each individual step taken is in a rondom direction. It shows \n" 
+ "both the starting and ending point and each point that was walked on.\n\n" 
+ "----------------------------------------------------------------\n\n"
+ "Enter your desired number of steps to show: "))

# Keep making new walks, as long as the program is active.
while True: # program loop
    # Make a random walk.
    rw = RandomWalk(user_num_points)
    rw.fill_walk() # Calculate all the points in the walk.

    # Plot the points in the walk.
    plt.style.use('dark_background')

    fig, ax = plt.subplots(figsize=(9, 6)) # set window to wide rectangle

    point_numbers = range(rw.num_points) # number of points for the Scatter Graph

    # Create Scatter Graph using class data values, number of points, 
    #  colormap (plasma), no assigned edge point colors, and size=1
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.plasma,
        edgecolors='none', s=1)

    # # Emphasize the first and last points.

    # First point at 0,0, chartreuse colored, edge is fuchsia, and size is 88
    ax.scatter(0, 0, c='chartreuse', edgecolors='fuchsia', s=88) 

    # Last point at final location deeppink colored, edge is lavender, and size is 120
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='deeppink', edgecolors='lavender',
        s=120)

    # Remove the axes.
    ax.get_xaxis().set_visible(False) # Hide X-Axis
    ax.get_yaxis().set_visible(False) # Hide Y-Axis

    plt.show() # Show the Scatter Graph

    # looping variable from user input
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n': # if n is entered leave program loop
        break
