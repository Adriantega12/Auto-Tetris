'''Module for CSV data file creation'''

import csv

class DataGenerator:
    '''CSV class interface to keep continues growing data on a CSV file'''

    def __init__(self, create_new=False, file_name='Data.csv'):
        self.csv_file = open(
            file_name,
            'w' if create_new else 'a',
            )
        self.writer = csv.writer(self.csv_file)

        if create_new:
            header = [i for i in range(22 * 10)]
            header.append('Output')
            self.writer.writerow(header)

    def __del__(self):
        self.csv_file.close()

    def write_grid(self, grid, move):
        '''Writes instance of grid in a given frame'''
        row = []
        for i in range(grid.height):
            for j in range(grid.width):
                row.append(int(grid[i][j] > 0))

        row.append(move)
        self.writer.writerow(row)
