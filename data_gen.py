import csv

class DataGenerator:
    def __init__(self, file_name='Data.csv'):
        self.csv_file = open(file_name, 'w')
        self.writer = csv.writer(self.csv_file)
        header = [i for i in range(22 * 10)]
        header.append('Output')
        self.writer.writerow(header)

    def __del__(self):
        self.close_file()

    def write_grid(self, grid, move):
        ''''''
        row = []
        for i in range(grid.height):
            for j in range(grid.width):
                row.append(int(grid[i][j] > 0))

        row.append(move)
        self.writer.writerow(row)

    def close_file(self):
        '''Close file after usage'''
        self.csv_file.close()
