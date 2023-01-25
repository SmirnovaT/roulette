from collections import deque
from random import randrange


class Game():

    def start(self):
        self.__hi()
        self.__revolver_do()
        for i in range(self.player):
            self.__game()
            if self.patron == self.drum:
                print(f"{i + 1}-й игрок убит! Игра завершена.")
                break
            if self.patron != self.drum:
                print(f"{i + 1}-й игрок выиграл!")
                if i + 1 == self.player:
                    print("Конец игры")
                else:
                    print('Продолжаем играть ;)')
                    self.revolver.rotate(-1)
                    print("Нажмите Enter, чтобы передать револьвер другому игроку.")
                    self.give_revolver = input()

    def __hi(self):
        print("Добро пожаловать в игру рулетку!\nCколько игроков будет участвовать?")
        self.player = int(input())

    def __revolver_do(self):
        print("Pевольвер зарядили!")
        self.revolver = deque([False for i in range(6)])
        self.patron = randrange(0, 6)
        self.revolver[self.patron] = True

    def __game(self):
        print("Крутится барабан... Нажмите Enter, чтобы остановить барабан.")
        self.stop_drum = input()
        self.drum = randrange(0, 6)
        print("Стреляйте! Нажмите Enter")
        self.shoot = input()
