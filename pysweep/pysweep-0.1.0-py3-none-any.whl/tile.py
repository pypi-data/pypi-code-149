class Tile:
    coordinates = []
    mine = False
    popped = False

    def __init__(self, coordinates: list, mine: bool = False):
        self.coordinates = coordinates
        self.mine = mine

    def __str__(self):
        if self.mine:
            return f'Mine: {self.coordinates}'
        return f'Tile: {self.coordinates}'

    def pop_tile(self):
        self.popped = True

    def calculate_tile_number(self, minefield):
        if not self.popped:
            return '#'
        if self.mine:
            return 'X'
        number_of_mines = 0
        tiles_to_find = [
            [self.coordinates[0]+1, self.coordinates[1]],
            [self.coordinates[0], self.coordinates[1]+1],
            [self.coordinates[0]+1, self.coordinates[1]+1],
            [self.coordinates[0]-1, self.coordinates[1]],
            [self.coordinates[0], self.coordinates[1]-1],
            [self.coordinates[0]-1, self.coordinates[1]-1],
            [self.coordinates[0]+1, self.coordinates[1]-1],
            [self.coordinates[0]-1, self.coordinates[1]+1]
        ]
        for tile in minefield.tiles:
            for i in range(len(tiles_to_find)):
                if tile.coordinates == tiles_to_find[i] and tile.mine:
                    number_of_mines += 1
                    break
        return number_of_mines
