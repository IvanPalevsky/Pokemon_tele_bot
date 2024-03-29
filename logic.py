from random import randint
from datetime import datetime, timedelta
import requests
import time

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(10, 100)
        self.power = randint(10, 30)
        self.last_feed_time = datetime.now

        Pokemon.pokemons[pokemon_trainer] = self
    
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['home']['front_default'])
        else:
            return "data:image/png;base64,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"

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
сила покемона {self.power}
здоровье покемона {self.hp}
"""
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"  

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\n Боец применил супер-атаку силой:{super_power} "

class Wizard(Pokemon):
    def feed_self():
        return super().feed(10)

p = Pokemon('user1')
time.sleep(21)
print(p.feed())




