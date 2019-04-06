'''
Main file, the game should be ran from here.
'''
from game_manager import GameManager

def main():
    '''Main function that gets called when the game is started'''
    gm = GameManager()

    gm.loop()


if __name__ == '__main__':
    main()
