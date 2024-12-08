class CalibrationWizard:
    OPERATORS_PART1 = {
        '➕': lambda x, y: x + y,
        '✖️': lambda x, y: x * y
    }
    
    OPERATORS_PART2 = {
        '➕': lambda x, y: x + y,
        '✖️': lambda x, y: x * y,
        '🔗': lambda x, y: int(f'{x}{y}')
    }

class EquationSolver:
    def __init__(self, equation_data, operators):
        self.test_value, numbers = equation_data.split(':')
        self.test_value = int(self.test_value)
        self.numbers = [int(n) for n in numbers.strip().split()]
        self.operators = operators
    
    def try_combinations(self):
        operators = list(self.operators.keys())
        needed_ops = len(self.numbers) - 1
        
        def evaluate(ops):
            result = self.numbers[0]
            for i, op in enumerate(ops):
                result = self.operators[op](result, self.numbers[i + 1])
            return result
        
        def generate_combinations(current=[]):
            if len(current) == needed_ops:
                return evaluate(current) == self.test_value
            
            return any(
                generate_combinations(current + [op])
                for op in operators
            )
        
        return generate_combinations()

def calibrate_bridge(filename, operators):
    with open(filename, 'r') as f:
        equations = [EquationSolver(line.strip(), operators) for line in f.readlines()]
    
    valid_equations = [eq.test_value for eq in equations if eq.try_combinations()]
    return sum(valid_equations)

if __name__ == '__main__':
    print('🐘 Time to solve some equations! 🌴')
    print('Part 1: Basic operators (➕, ✖️)')
    print(f'🔧 Calibration result: {calibrate_bridge("2024.txt", CalibrationWizard.OPERATORS_PART1)} 🎯')
    print('\nPart 2: With concatenation (➕, ✖️, 🔗)')
    print(f'🔧 Updated calibration result: {calibrate_bridge("2024.txt", CalibrationWizard.OPERATORS_PART2)} 🎯')
