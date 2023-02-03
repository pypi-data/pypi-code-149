from .minefield import Minefield
import os


class Sweeper:
    minefield = Minefield()

    def __init__(self, minefield):
        self.minefield = minefield

    # @staticmethod
    def sweep_tile(self, x_coordinate, y_coordinate):
        coordinates = [x_coordinate, y_coordinate]
        for tile in self.minefield.tiles:
            if coordinates == tile.coordinates:
                tile.pop_tile()
                if tile.mine:
                    print("Bang!")
                    self.game_over()
                    break
        os.system('clear')
        self.minefield.draw_minefield()
        self.get_user_coordinate_input()

    def restart(self):
        self.minefield = Minefield(width=10, height=10, number_of_mines=10)
        self.minefield.generate_tiles()
        self.minefield.place_mines()

    def game_over(self):
        os.system('clear')
        self.minefield.draw_minefield()
        print('Game over')
        input('Press [ENTER] to return to restart.')
        self.restart()
        os.system('clear')

    def main_menu(self):
        os.system('clear')
        print('Welcome to MineSweeper')
        input('Press [ENTER] to start.')
        os.system('clear')
        self.minefield.draw_minefield()
        self.get_user_coordinate_input()

    def get_user_coordinate_input(self):
        while True:
            try:
                coordinates = input('Input coordinates: ').split(' ')
                x_coordinate = int(coordinates[0])
                y_coordinate = int(coordinates[1])
                if len(coordinates) > 2:
                    raise ValueError
            except (ValueError, IndexError):
                print("Inputted coordinates are invalid, try again.")
                continue
            else:
                break
        self.sweep_tile(x_coordinate, y_coordinate)
