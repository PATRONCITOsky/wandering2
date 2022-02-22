from wandering import ComunWandering
from track import Track 
from location import Location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering, steps):
    beginning = location.get_location(wandering)
    
    for _ in range(steps):
        location.move_wandering(wandering)
    
    return beginning.distance(location.get_location(wandering))