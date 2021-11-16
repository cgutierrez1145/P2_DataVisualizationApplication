from random import choice

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
    
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
        
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1]) # randomly go left or right
            x_distance = choice([0, 1, 2, 3, 4]) # randomly go a distance from 0-4
            x_step = x_direction * x_distance # store data
        
            y_direction = choice([1, -1]) # randomly go up or down
            y_distance = choice([0, 1, 2, 3, 4]) # randomly go distance from 0-4
            y_step = y_direction * y_distance # store data
        
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0: # random distances were 0
                continue # leave current execution of loop, but not entire loop
        
            # Calculate the new position.
            x = self.x_values[-1] + x_step # move left or right for current position
            y = self.y_values[-1] + y_step # move up or down for current position
        
            self.x_values.append(x) # store to list of all x coordinates
            self.y_values.append(y) # store to list of all y coordinates
