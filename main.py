from roulette import Game

Game.hi()
Game.revolver_do()

for i in range(Game.player):
    Game.game()
    if Game.patron == Game.drum:
        print(f"{i + 1}-й игрок убит! Игра завершена.")
        break
    if Game.patron != Game.drum:
        print(f"{i + 1}-й игрок выиграл!")

        if i + 1 == Game.player:
            print("Конец игры")
        else:
            print('Продолжаем играть ;)')
            Game.revolver.rotate(-1)
            print("Нажмите Enter, чтобы передать револьвер другому игроку.")
            Game.give_revolver = input()
