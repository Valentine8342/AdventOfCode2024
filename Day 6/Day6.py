class TimeDevice:
    MOVES = {'⬆️': (0, -1, '➡️'), '➡️': (1, 0, '⬇️'), '⬇️': (0, 1, '⬅️'), '⬅️': (-1, 0, '⬆️')}

class TimelineSimulator:
    def __init__(self, map_data):
        self.map = map_data
        self.height, self.width = len(map_data), len(map_data[0])
        self.start = next((
            (x, y) for y in range(self.height) for x in range(self.width)
            if map_data[y][x] == '👮'
        ), None)
    
    def simulate(self, target=None, track_visited=False):
        if not self.start:
            return (False, set())
        
        x, y = self.start
        direction = '⬆️'
        visited = set()
        path_positions = set()
        steps = 0
        
        while steps < 10000:
            state = (x, y, direction)
            if state in visited:
                return (True, path_positions)
            visited.add(state)
            if track_visited:
                path_positions.add((x, y))
            
            dx, dy, next_dir = TimeDevice.MOVES[direction]
            next_x, next_y = x + dx, y + dy
            
            if not (0 <= next_x < self.width and 0 <= next_y < self.height):
                return (False, path_positions)
                
            if self.map[next_y][next_x] == '🚧' or (target and (next_x, next_y) == target):
                direction = next_dir
            else:
                x, y = next_x, next_y
            
            steps += 1
            
        return (False, path_positions)

def analyze_timestream(filename):
    CHARS = {'^': '👮', '#': '🚧', '.': '⬜', '*': '📦', 'x': '🎯'}
    with open(filename, 'r') as f:
        map_data = [[CHARS.get(c, c) for c in line.strip()] for line in f.readlines()]
    
    sim = TimelineSimulator(map_data)
    
    _, visited_positions = sim.simulate(track_visited=True)
    part1_result = len(visited_positions)
    
    part2_result = sum(1 for y in range(sim.height) for x in range(sim.width)
                      if map_data[y][x] == '⬜' and (x, y) != sim.start 
                      and sim.simulate((x, y))[0])
    
    return part1_result, part2_result

if __name__ == '__main__':
    print('✨ Initializing Time Machine... ⚡')
    part1, part2 = analyze_timestream("2024.txt")
    print(f'🔮 Part 1: Guard will visit {part1} distinct positions! 🚶')
    print(f'🔮 Part 2: Found {part2} possible positions for stable time loops! 🌀')