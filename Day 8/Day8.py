class AntennaMappa:
    def __init__(self, mapData):
        self.mapData = mapData
        self.height = len(mapData)
        self.width = len(mapData[0]) if self.height > 0 else 0
        self.emoji = {}
        self.antennas = self._sniffOutChocolateAntennas()

    def _sniffOutChocolateAntennas(self):
        frequencies = set(''.join(self.mapData)) - {'.'}
        antennas = {}
        for freq in frequencies:
            self.emoji['📡'] = freq
            positions = []
            for y in range(self.height):
                self.emoji['🔽'] = y
                for x in range(self.width):
                    self.emoji['➡️'] = x
                    if self.mapData[self.emoji['🔽']][self.emoji['➡️']] == self.emoji['📡']:
                        positions.append((self.emoji['➡️'], self.emoji['🔽']))
            antennas[self.emoji['📡']] = positions
        return antennas

    def _isThisRoofTileReal(self, x, y):
        self.emoji['➡️'] = x
        self.emoji['🔽'] = y
        return 0 <= self.emoji['➡️'] < self.width and 0 <= self.emoji['🔽'] < self.height

    def gimmeTheChocolate(self):
        self.emoji['🎄'] = set()
        for freq, positions in self.antennas.items():
            self.emoji['📡'] = freq
            self.emoji['🔢'] = len(positions)
            for i in range(self.emoji['🔢']):
                self.emoji['🎅'] = i
                self.emoji['➡️1'], self.emoji['🔽1'] = positions[self.emoji['🎅']]
                for j in range(self.emoji['🎅'] + 1, self.emoji['🔢']):
                    self.emoji['🦌'] = j
                    self.emoji['➡️2'], self.emoji['🔽2'] = positions[self.emoji['🦌']]
                    self.emoji['🎁1'] = (2 * self.emoji['➡️1'] - self.emoji['➡️2'], 2 * self.emoji['🔽1'] - self.emoji['🔽2'])
                    self.emoji['🎁2'] = (2 * self.emoji['➡️2'] - self.emoji['➡️1'], 2 * self.emoji['🔽2'] - self.emoji['🔽1'])
                    for x, y in (self.emoji['🎁1'], self.emoji['🎁2']):
                        self.emoji['➡️'], self.emoji['🔽'] = x, y
                        if self._isThisRoofTileReal(self.emoji['➡️'], self.emoji['🔽']):
                            self.emoji['🎄'].add((self.emoji['➡️'], self.emoji['🔽']))
        return self.emoji['🎄']

    def gimmeTheExtraChocolate(self):
        self.emoji['🎄'] = set()
        for freq, positions in self.antennas.items():
            self.emoji['📡'] = freq
            self.emoji['🔢'] = len(positions) 
            for i in range(self.emoji['🔢']):
                self.emoji['🎅'] = i
                self.emoji['➡️1'], self.emoji['🔽1'] = positions[self.emoji['🎅']]
                for j in range(self.emoji['🎅'] + 1, self.emoji['🔢']):
                    self.emoji['🦌'] = j
                    self.emoji['➡️2'], self.emoji['🔽2'] = positions[self.emoji['🦌']]
                    self.emoji['d➡️'], self.emoji['d🔽'] = self.emoji['➡️2'] - self.emoji['➡️1'], self.emoji['🔽2'] - self.emoji['🔽1']
                    self.emoji['➡️'], self.emoji['🔽'] = self.emoji['➡️1'], self.emoji['🔽1']
                    while self._isThisRoofTileReal(self.emoji['➡️'], self.emoji['🔽']):
                        self.emoji['🎄'].add((self.emoji['➡️'], self.emoji['🔽']))
                        self.emoji['➡️'] += self.emoji['d➡️']
                        self.emoji['🔽'] += self.emoji['d🔽']
                    self.emoji['➡️'], self.emoji['🔽'] = self.emoji['➡️1'] - self.emoji['d➡️'], self.emoji['🔽1'] - self.emoji['d🔽']
                    while self._isThisRoofTileReal(self.emoji['➡️'], self.emoji['🔽']):
                        self.emoji['🎄'].add((self.emoji['➡️'], self.emoji['🔽']))
                        self.emoji['➡️'] -= self.emoji['d➡️']
                        self.emoji['🔽'] -= self.emoji['d🔽']
        return self.emoji['🎄']

class ChocolateResonanceAnalyzer:
    @staticmethod
    def decodeTheEasterBunnyMischief(filename):
        try:
            with open(filename, 'r') as file:
                mapData = [line.strip() for line in file]
        except IOError as error:
            raise Exception(f'Oops, the Easter Bunny hid the file {filename}: {error}')
        
        mapper = AntennaMappa(mapData)
        antinodes_part1 = mapper.gimmeTheChocolate()
        antinodes_part2 = mapper.gimmeTheExtraChocolate()
        return len(antinodes_part1), len(antinodes_part2)

if __name__ == '__main__':
    print('🐰 Time to foil the Easter Bunny\'s chocolate scheme! 🍫')
    result_part1, result_part2 = ChocolateResonanceAnalyzer.decodeTheEasterBunnyMischief('2024.txt')
    print('Part 1: Basic Chocolate Wave Detection')
    print(f'📊 Chocolate Wave Hotspots: {result_part1} unique spots of chocolatey mischief! 🎯')
    print('\nPart 2: Advanced Gooey Chocolate Wave Detection')
    print(f'📊 Super Gooey Chocolate Hotspots: {result_part2} unique spots of extreme chocolatey mayhem! 🎯')
