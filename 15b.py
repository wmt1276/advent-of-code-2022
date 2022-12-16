from aoc import get_input
from aocd import submit
import numpy

day = 15

def get_distance(sensor: tuple, beacon: tuple):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

def main(data: list):
    sensors = []
    beacons = []
        
    target = 4000000
    
    for line in data:   # Iterate Over Each Line in Data
        parts = line.split(': closest beacon is at x=')
        
        parts[0] = parts[0][len('Sensor at x='):]
        
        sensor = parts[0].split(', y=')
        beacon = parts[1].split(', y=')
        
        sensors.append((int(sensor[0]), int(sensor[1])))
        beacons.append((int(beacon[0]), int(beacon[1])))
        
    for x in numpy.arange(target + 1):
        
        y = 0
        while y <= target:
            blocked = False
            for index in numpy.arange(len(sensors)):
                beacon_distance = get_distance(sensors[index], beacons[index])
                
                sensor_distance = get_distance((x, y), sensors[index])
                
                distance_differential = beacon_distance - sensor_distance
                
                if distance_differential >= 0:
                    y = sensors[index][1] + abs(sensors[index][1] - y) + distance_differential
                    
                    blocked = True
                    break
                
            if not blocked:
                return (4000000 * x) + y
            
            y += 1

if __name__ == '__main__':
    data = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''.splitlines()

    # Get Input Data
    data = get_input(day).splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0, 56000011]:
        submit(answer, part='b', day=day, year=2022)
    else:
        print('No Answer Submitted')