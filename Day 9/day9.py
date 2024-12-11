from itertools import chain

class DiskCompactionManager:
    def __init__(self):
        self.disk = {}
        self.disk['📖'] = lambda file_path: open(file_path, 'r').read().strip()

    def solve_part1(self, input_data):
        self.disk['💾'] = list(map(int, input_data))
        self.disk['📁'] = self.disk['💾'][::2]
        self.disk['🆓'] = self.disk['💾'][1::2]

        self.disk['🏷️'] = []
        for index, file in enumerate(self.disk['📁']):
            self.disk['🏷️'].extend([str(index)] * file)

        self.disk['🗄️'] = []
        for a, b in zip(self.disk['📁'], self.disk['🆓']):
            for _ in range(a):
                if self.disk['🏷️']:
                    self.disk['🗄️'].append(self.disk['🏷️'].pop(0))
            for _ in range(b):
                if self.disk['🏷️']:
                    self.disk['🗄️'].append(self.disk['🏷️'].pop())

        while self.disk['🏷️']:
            self.disk['🗄️'].append(self.disk['🏷️'].pop(0))

        self.disk['🧮'] = sum(index * int(block) for index, block in enumerate(self.disk['🗄️']))
        return self.disk['🧮']

    def solve_part2(self, input_data):
        self.disk['💾'] = list(map(int, input_data))
        self.disk['🗄️'] = []
        self.disk['🆔'] = 0
        self.disk['🔓'] = False

        for number in self.disk['💾']:
            if number != 0:
                self.disk['🗄️'].append(['.' if self.disk['🔓'] else str(self.disk['🆔'])] * number)
            if not self.disk['🔓']:
                self.disk['🆔'] += 1
            self.disk['🔓'] = not self.disk['🔓']

        for file in self.disk['🗄️'][::-1]:
            if '.' in file:
                continue
            self.disk['📍'] = self.disk['🗄️'].index(file)
            self.disk['🕳️'] = [b for b in self.disk['🗄️'] if '.' in b and b.count('.') >= len(file)]
            if self.disk['🕳️']:
                self.disk['🕳️📍'] = self.disk['🗄️'].index(self.disk['🕳️'][0])
                if self.disk['📍'] < self.disk['🕳️📍']:
                    continue
                self.disk['🆓📍'] = self.disk['🕳️'][0].index('.')
                for i in range(len(file)):
                    self.disk['🕳️'][0][i + self.disk['🆓📍']] = file[i]
                    file[i] = '.'

        self.disk['🗄️'] = list(chain.from_iterable(self.disk['🗄️']))
        self.disk['🧮'] = sum(int(number) * index for index, number in enumerate(self.disk['🗄️']) if number.isdigit())
        return self.disk['🧮']

def main():
    manager = DiskCompactionManager()
    manager.disk['📥'] = manager.disk['📖']('2024.txt')
    
    manager.disk['1️⃣'] = manager.solve_part1(manager.disk['📥'])
    print(f"Result Part 1: {manager.disk['1️⃣']}")
    
    manager.disk['2️⃣'] = manager.solve_part2(manager.disk['📥'])
    print(f"Result Part 2: {manager.disk['2️⃣']}")

if __name__ == "__main__":
    main() 