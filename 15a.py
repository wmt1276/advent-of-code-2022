from aoc import get_input
from aocd import submit

day = 15

def get_distance(sensor: tuple, beacon: tuple):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

def main(data: list):
    sensors = []
    beacons = []
    
    for line in data:   # Iterate Over Each Line in Data
        parts = line.split(': closest beacon is at x=')
        
        parts[0] = parts[0][len('Sensor at x='):]
        
        sensor = parts[0].split(', y=')
        beacon = parts[1].split(', y=')
        
        sensors.append((int(sensor[0]), int(sensor[1])))
        beacons.append((int(beacon[0]), int(beacon[1])))
        
    row = set()
    
    target = 2000000
    
    for index in range(len(sensors)):
        distance = get_distance(sensors[index], beacons[index])
        
        if target in range(sensors[index][1] - distance, sensors[index][1] + distance + 1):
            searched = True
            dx = 0
            while searched:
                if get_distance(sensors[index], (sensors[index][0] + dx, target)) <= distance:
                    row.add((sensors[index][0] + dx, target))
                    row.add((sensors[index][0] - dx, target))
                    dx += 1
                else:
                    searched = False
                    
    blocked = len(row)
    beacon_set = set(beacons)
                    
    for beacon in beacon_set:
        if beacon in row:
            blocked -= 1

    return blocked

if __name__ == '__main__':
    # Get Input Data
    data = get_input(day).splitlines()
    
#     data = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3'''.splitlines()
    
    answer = main(data)
    # Print Answer
    print(answer)
    
    if answer not in [None, '', 0]:
        submit(answer, part='a', day=day, year=2022)
    else:
        print('No Answer Submitted')