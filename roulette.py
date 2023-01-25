from collections import deque
from random import randrange


class Game:
    player = None
    patron = None
    stop_drum = None
    shoot = None
    drum = None
    revolver = None
    give_revolver = None

    @classmethod
    def hi(cls):
        print("Добро пожаловать в игру рулетку!\nCколько игроков будет участвовать?")
        cls.player = int(input())

    @classmethod
    def revolver_do(cls):
        print("Pевольвер зарядили!")
        cls.revolver = deque([False for i in range(6)])
        cls.patron = randrange(0, 6)
        cls.revolver[cls.patron] = True

    @classmethod
    def game(cls):
        print("Крутится барабан... Нажмите Enter, чтобы остановить барабан.")
        cls.stop_drum = input()
        cls.drum = randrange(0, 6)
        print("Стреляйте! Нажмите Enter")
        cls.shoot = input()
