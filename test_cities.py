import pytest
from cities import *


def test_compute_total_distance():
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    assert compute_total_distance(road_map)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

def test_compute_total_distance_two_cities():
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755)]
    assert compute_total_distance(road_map)==\
           pytest.approx(9.386+9.386, 0.01)




# def test_compute_total_distance_float():
#     """
#     Tests if the returned value is float.
#     """
#     road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
#                 ("Delaware", "Dover", 39.161921, -75.526755),
#                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
#     assert compute_total_distance(road_map1) == float


# def test_swap_cities_tuple():
#     """Tests if the returned value is a tuple.
#     Take the city at location `index` in the `road_map`, and the 
#     city at location `index2`, swap their positions in the `road_map`, 
#     compute the new total distance, and return the tuple 

#         (new_road_map, new_total_distance)

#     Allow for the possibility that `index1=index2`,
#     and handle this case correctly.
#     """
#     road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
#                 ("Delaware", "Dover", 39.161921, -75.526755),
#                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
#     assert swap_cities(road_map1, 1, 2) == tuple


# def test_shift_cities_different():
#     """
#     Tests that the first road map is different from the shifted one.
#     For every index i in the `road_map`, the city at the position i moves
#     to the position i+1. The city at the last position moves to the position
#     0. Return the new road map. 
#     """
#     road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
#                 ("Delaware", "Dover", 39.161921, -75.526755),
#                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
#     if len(road_map1)>1:
#     	assert road_map1 != shift_cities(road_map1)

#     else:
#     	assert shift_cities(road_map1) == road_map1


