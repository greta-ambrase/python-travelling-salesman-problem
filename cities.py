import math
import copy
import random
import matplotlib.pyplot as plt

def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    file = open(file_name, 'r')
    road_map = []
    for i in file.readlines():
        line = i.strip('\n')
        tmp = line.split('\t')
        road_map.append(tuple((tmp[0], tmp[1], float(tmp[2]), float(tmp[3]))))
        
    return road_map

  
def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    for i in road_map:
        for j in i:
            if type(j) == float:
                print(f'{j:0.2f}', end =', ')
            else:
                print(j, end = ', ')
        print('\n')


def compute_total_distance(road_map):
#     """
#     Returns, as a floating point intber, the sum of the distances of all 
#     the connections in the `road_map`. Remember that it's a cycle, so that 
#     (for example) in the initial `road_map`, Wyoming connects to Alabama...
#     """

    total_distance = 0

    #calculate the Euclidian distance between cities road_map[n] and road_map[n+1]. This excludes the last city.
    for i in range(0,len(road_map)-1):

        x1 = road_map[i][2]
        x2 = road_map[i][3]
        y1 = road_map[i+1][2]
        y2 = road_map[i+1][3]

        distance = math.sqrt((x1-y1)**2 + (x2-y2)**2)
        total_distance+=distance

    #calculate the distance between the last city and the first.
    x1 = road_map[-1][2]
    x2 = road_map[-1][3]
    y1 = road_map[0][2]
    y2 = road_map[0][3]

    distance = math.sqrt((x1-y1)**2 + (x2-y2)**2)
    total_distance+=distance

    return total_distance
    


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    x1 = road_map[index1]
    x2 = road_map[index2]

    road_map[index1] = x2
    road_map[index2] = x1

    return (road_map,compute_total_distance(road_map))


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    if len(road_map) == 1:
    	return road_map

    else:
	    shifted_road_map = []

	    x_first = road_map[0]
	    x_last = road_map[-1]

	    shifted_road_map.append(x_last)
	    shifted_road_map.append(x_first)

	    for i in range(1, len(road_map)-1):
	    	shifted_road_map.append(road_map[i])

	    return shifted_road_map

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    best_distance = compute_total_distance(road_map)
    best_map = road_map
    n = 10000
    random.seed(10000)

    for i in range(0,n):
    	new_map = copy.deepcopy(best_map)

    	new_map = shift_cities(new_map)

    	index1 = random.randint(0,(len(road_map)-1))
    	index2 = random.randint(0,(len(road_map)-1))
    	new_map = swap_cities(new_map, index1, index2)[0]

    	new_distance = compute_total_distance(new_map)

    	if new_distance < best_distance:
    		best_distance = new_distance
    		best_map = new_map

    return best_map


def print_map(road_map):
	"""
	Prints, in an easily understandable format, the cities and 
	their connections, along with the cost for each connection 
	and the total cost.
	matplotlib
	"""
	d = []

	for i in range(0,len(road_map)-1):
		cities = str(road_map[i][0]) + ' ' + str(road_map[i][1]) +' and ' + str(road_map[i+1][0]) + ' ' + str(road_map[i+1][1]) + ': '
		distance = math.sqrt((road_map[i][2]-road_map[i+1][2])**2 + (road_map[i][3]-road_map[i+1][3])**2)
		d.append((cities, f'{distance:0.2f}'))

	distance = math.sqrt((road_map[-1][2]-road_map[0][2])**2 + (road_map[-1][3]-road_map[0][3])**2)
	cities = str(road_map[-1][0]) + ' ' + str(road_map[-1][1]) +' and ' + str(road_map[0][0]) + ' ' + str(road_map[0][1]) + ': '
	d.append((cities, f'{distance:0.2f}'))

	for i in d:
		print(i[0], i[1])

	print('Total distance: ' + str(compute_total_distance(road_map)))


	#line, = plt.plot([i[2] for i in road_map], [i[3] for i in road_map], 'go-')
	plt.plot([i[3] for i in road_map], [i[2] for i in road_map], 'go-')
	#plt.text([[i[2] for i in road_map], [i[3] for i in road_map]], d, fontsize =12)

	plt.show()


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    road_map=read_cities('city-data.txt')
    print_cities(road_map)

    best_map = find_best_cycle(road_map)

    print_map(best_map)


if __name__ == "__main__": #keep this in
	main()

