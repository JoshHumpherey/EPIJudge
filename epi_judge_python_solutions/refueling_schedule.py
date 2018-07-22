import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20
class car:
    def __init__(self, tank, mpg):
        self.tank = tank
        self.mpg = mpg
class station:
    def __init__(self, next_leg, fuel):
        self.next_leg = next_leg
        self.fuel = fuel

def find_ample_city(gallons, distances):
    city_list = []
    for i in range(len(gallons)):
        my_station = station(gallons[i], distances[i])
        city_list.append(my_station)

    for i in range(len(city_list)):
        first = city_list.pop(0)
        city_list.append(first) # keep the cities cycling
        my_car = car(0, 20)
        for stop in city_list:
            my_car.tank += stop.fuel
            possible_distance = (my_car.tank)*(my_car.mpg)
            if possible_distance > stop.next_leg:
                print("traveling")
                difference = possible_distance - stop.next_leg
                leftover = difference / my_car.mpg
                my_car.tank = leftover
                if stop == city_list[-1]:
                    return stop.next_leg
            else:
                print("Station failed")
                break





@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of fuel on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("refueling_schedule.py",
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
