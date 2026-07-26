# game.py
import random
import time
from constans import *
from cell import Cell
from helicopter import Helicopter
from utils import clear_screen, getch

class Game:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.field = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.helicopter = Helicopter(cols//2, rows//2)
        self.weather = 'clear'
        self.weather_timer = 0
        self.running = True
        self.paused = False

    def generate_rivers(self, count=2):
        for _ in range(count):
            x = random.randint(1, self.cols-2)
            y = random.randint(1, self.rows-2)
            length = random.randint(self.cols//3, self.cols//2)
            dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
            for _ in range(length):
                if 0 <= x < self.cols and 0 <= y < self.rows:
                    self.field[y][x].type = 'river'
                    if random.random() < 0.3:
                        dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
                    x += dx
                    y += dy
                else:
                    break

    def generate_trees(self, density=0.15):
        for y in range(self.rows):
            for x in range(self.cols):
                if self.field[y][x].type == 'empty' and random.random() < density:
                    self.field[y][x].type = 'tree'
                    self.field[y][x].tree_alive = True
                    self.field[y][x].growth = random.randint(20, 100)

    def generate_hospital_and_shop(self):
        placed = 0
        while placed < 2:
            x = random.randint(1, self.cols-2)
            y = random.randint(1, self.rows-2)
            if self.field[y][x].type == 'empty':
                self.field[y][x].type = 'hospital' if placed == 0 else 'shop'
                placed += 1

    def tick_grow(self):
        for y in range(self.rows):
            for x in range(self.cols):
                cell = self.field[y][x]
                if cell.type == 'tree' and cell.tree_alive:
                    cell.growth = min(100, cell.growth + random.randint(1, 5))
                    if cell.growth >= 100 and random.random() < TREE_GROW_CHANCE:
                        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < self.cols and 0 <= ny < self.rows:
                                if self.field[ny][nx].type == 'empty':
                                    self.field[ny][nx].type = 'tree'
                                    self.field[ny][nx].tree_alive = True
                                    self.field[ny][nx].growth = 10
                                    break

    def tick_fire(self):
        fire_chance = WEATHER_CHANCE * 2 if self.weather == 'thunder' else WEATHER_CHANCE
        if random.random() < fire_chance:
            x = random.randint(0, self.cols-1)
            y = random.randint(0, self.rows-1)
            if self.field[y][x].type == 'tree' and self.field[y][x].tree_alive and not self.field[y][x].on_fire:
                self.field[y][x].on_fire = True

        new_fires = []
        for y in range(self.rows):
            for x in range(self.cols):
                if self.field[y][x].on_fire:
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < self.cols and 0 <= ny < self.rows:
                            cell = self.field[ny][nx]
                            if cell.type == 'tree' and cell.tree_alive and not cell.on_fire:
                                if random.random() < FIRE_SPREAD_CHANCE:
                                    new_fires.append((nx, ny))
        for x, y in new_fires:
            self.field[y][x].on_fire = True

        for y in range(self.rows):
            for x in range(self.cols):
                if self.field[y][x].on_fire:
                    if self.weather == 'rain' and random.random() < 0.3:
                        self.field[y][x].on_fire = False
                        self.field[y][x].type = 'burnt'
                        self.field[y][x].tree_alive = False
                        self.helicopter.points += PENALTY_PER_BURNT
                    elif random.random() < 0.1:
                        self.field[y][x].on_fire = False
                        self.field[y][x].type = 'burnt'
                        self.field[y][x].tree_alive = False
                        self.helicopter.points += PENALTY_PER_BURNT

    def tick_weather(self):
        self.weather_timer -= 1
        if self.weather_timer <= 0:
            self.weather = random.choice(['clear', 'clear', 'clear', 'rain', 'thunder'])
            self.weather_timer = random.randint(10, 30)

    def render(self):
        clear_screen()
        print(f"❤️ Health: {self.helicopter.health}  💧 Water: {self.helicopter.water}/{self.helicopter.max_water}  ⭐ Points: {self.helicopter.points}")
        print(f"☁️ Weather: {self.weather}  (SPACE: act, WASD: move, P: pause, Q: quit, O: save, L: load)")
        print("  " + "".join(f"{i:2}" for i in range(self.cols)))
        for y in range(self.rows):
            line = f"{y:2} "
            for x in range(self.cols):
                if self.helicopter.x == x and self.helicopter.y == y:
                    line += HELICOPTER
                else:
                    line += str(self.field[y][x])
            print(line)

    def handle_input(self):
        key = getch().lower()
        if key == 'q':
            self.running = False
        elif key == 'p':
            self.paused = not self.paused
        elif self.paused:
            return
        elif key == 'w':
            self.helicopter.move(0, -1, self.field)
        elif key == 's' and not self.paused:  # но 's' ещё и сохранение, поэтому сделаем отдельно
            # мы не можем использовать 's' для движения вниз и сохранения, поэтому я поменяю:
            # движение вниз будет на стрелку вниз, но у нас нет стрелок, поэтому используем 'x' для сохранения?
            # Лучше переделаем: движение вниз – клавиша 's', сохранение – 'S' (shift+s)
            # но getch() возвращает строчные, поэтому мы проверим на 'S' не получится.
            # Поэтому я сделаю сохранение на 'o' (от save), а загрузку на 'l'.
            pass  # мы реализуем ниже с другими клавишами, перепишем.

    def handle_input_fixed(self):
        """Исправленная обработка ввода с учётом конфликтов"""
        key = getch().lower()
        if key == 'q':
            self.running = False
        elif key == 'p':
            self.paused = not self.paused
        elif self.paused:
            return
        elif key == 'w':
            self.helicopter.move(0, -1, self.field)
        elif key == 's':
            self.helicopter.move(0, 1, self.field)
        elif key == 'a':
            self.helicopter.move(-1, 0, self.field)
        elif key == 'd':
            self.helicopter.move(1, 0, self.field)
        elif key == ' ':
            # действие
            if self.helicopter.take_water(self.field):
                pass
            elif self.helicopter.extinguish(self.field):
                pass
            elif self.helicopter.use_hospital(self.field):
                pass
            elif self.helicopter.use_shop(self.field):
                pass
        elif key == 'o':   # save (o = save)
            self.save_game()
        elif key == 'l':   # load
            self.load_game()

    def save_game(self, filename='savegame.json'):
        data = {
            'rows': self.rows,
            'cols': self.cols,
            'field': [],
            'helicopter': self.helicopter.to_dict(),
            'weather': self.weather,
            'weather_timer': self.weather_timer
        }
        for y in range(self.rows):
            row = []
            for x in range(self.cols):
                row.append(self.field[y][x].to_dict())
            data['field'].append(row)
        with open(filename, 'w') as f:
            import json
            json.dump(data, f, indent=2)
        print("Game saved!")

    def load_game(self, filename='savegame.json'):
        try:
            import json
            with open(filename, 'r') as f:
                data = json.load(f)
            self.rows = data['rows']
            self.cols = data['cols']
            self.field = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]
            for y in range(self.rows):
                for x in range(self.cols):
                    self.field[y][x] = Cell.from_dict(data['field'][y][x])
            self.helicopter = Helicopter.from_dict(data['helicopter'])
            self.weather = data['weather']
            self.weather_timer = data['weather_timer']
            print("Game loaded!")
        except FileNotFoundError:
            print("Save file not found.")

    def run(self):
        self.generate_rivers(3)
        self.generate_trees(0.2)
        self.generate_hospital_and_shop()
        self.weather_timer = 20

        while self.running:
            self.handle_input_fixed()
            if not self.paused and self.running:
                self.tick_grow()
                self.tick_fire()
                self.tick_weather()
                self.render()
                time.sleep(TICK_INTERVAL)

        print("Thanks for playing!")