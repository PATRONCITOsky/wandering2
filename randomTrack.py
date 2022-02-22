from turtle import distance
from wandering import ComunWandering, Wandering
from track import Track 
from location import Location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering, steps):
    beginning = location.get_location(wandering)
    
    for _ in range(steps):
        location.move_wandering(wandering)
    
    return beginning.distance(location.get_location(wandering))

def simulate_walk(steps, number_attemps, type_wandering):
    wandering = type_wandering(name='Alario')
    origen = Track(0,0)
    distances = []
    
    for _  in range(number_attemps):
        location = Location()
        location.add_wandering(Wandering, origen)
        simulations_walk = walking(location, wandering, steps)
        distances.append(round(simulations_walk, 1))
    return distances

def graph(x, y):
    graphics = figure(title='Camino del Errante', x_axis_label='Pasos', y_axis_label='Distancia')
    graphics.line(x, y, legend='Distancia')
    show(graphics)
    
def main(distances_walk, number_attemps, type_wandering):
    average_walking_distance = []
    
    for steps in distances_walk:
        distances = simulate_walk(steps, number_attemps, type_wandering)
        middle_distance = roun(sum(distances) / len(distances), 4)
        max_distances= max(distances)
        min_distances = min(distances)
        average_walking_distance.append(middle_distance)
        print(f'{type_wandering.__name__} Caminata aleatoria de {steps} pasos')
        print(f'Media = {middle_distance}')
        print(f'Max = {max_distances}')
        print(f'Min = {min_distances}')
    graph(distances_walk, average_walking_distance)
    
if __name__ == '__main__':
    distance_walk = [10, 100, 1000, 10000]
    number_attemps = 100
    main(distance_walk, number_attemps, ComunWandering)