import itertools
import time
import random

YES_ANSWERS = ('yes', 'y', 'yeah', 'yeap', 'ya')
NO_ANSWERS = ('no', 'nope', 'n')
ENEMIES_NAMES = ('Daryna Bereshnyk', 'Kate Voitushenko', 'Anastasia Khrush')

class Stalin:

    def __init__(self, *args, **kwargs):
        self.death_chance = 0.5
        self.enemies = []
        self.setup_default_names()
        self.body_chance = 0.5
        self.setup_names()
        self.animations = Animations()

    def setup_names(self):
        while True:
            name = input('Enter name convicted: ')
            surname = input('Enter surname convicted: ')
            new_enemy = Enemy(name=name, surname=surname)

            self.enemies.append(new_enemy)

            more_names = input('Do you want to add more name?: ')
            if more_names.lower() in NO_ANSWERS:
                break
            elif more_names.lower() in YES_ANSWERS:
                continue
            else:
                print('We deleted last person. Try again!')
                self.enemies.pop()
                print('\n')

    def repressions(self):
        while True:
            show_all = input('Do u want to check all names?: ')
            if show_all.lower() in YES_ANSWERS:
                self.show_all_enemies()
            selected_person = input('Enter ONE name for kill: ')
            enemy = self.target_available(selected_person)
            if enemy:
                if self.kill(enemy) == True:
                    self.show_all_enemies()
                else:
                    last_chance = input('Dietertir survived, but we need to do something with his life.' 
                        'Try again (last_chance) or keep alive? (yes - try again , no - keep alive): ')
                    if last_chance.lower() in YES_ANSWERS:
                        if self.kill(enemy) == True:
                            print('CONGATULATIONS. Dietertir WAS KILLED')
                            print('\n')
                            self.show_all_enemies()
                        else:
                            print('Ops, Dietertir was alive. Lets give for him one more chance for new life')
                            self.remove_from_enemies(enemy)
                    else:
                        print('I am disappointed in you')
                        self.remove_from_enemies(enemy)
            else:
                print('Sorry, check your name')
                self.show_all_enemies()
                print('All available targets')
                print('\n')
                error_more = input('Do you want again?: ')
                if error_more.lower() in YES_ANSWERS:
                    continue
                else:
                    break

            more = input('Do u want more?: ')
            if more.lower() in YES_ANSWERS:
                continue
            else:
                break

    def setup_default_names(self):
        for enemy_name in ENEMIES_NAMES:
            name, surname = enemy_name.split()
            new_enemy = Enemy(name=name, surname=surname)
            self.enemies.append(new_enemy)
        
    def show_all_enemies(self):
        print(';\n'.join([str(enemy) for enemy in self.enemies]))

    def target_available(self, search_term, return_person=False):
        for enemy in self.enemies:
            if enemy.name == search_term or enemy.surname == 'search_term':
                return enemy
        return False

    def kill(self, person):
        print(f'{person}, you are accused of treason')
        print('For this you should be shot')
        self.animations.animated_dots()
        survive_chance = random.random()
        if self.death_chance > survive_chance:
            self.remove_from_enemies(person)
            self.type_of_death(person)
            print('\n')
            return True
        else:
            print(f'{person} was survived')
            print('\n')
            return False

    def type_of_death(self, person):
        type_chance = random.random()
        if type_chance < self.body_chance:
            print(f'{person} was shot in the head. Death happened instantly')
        else:
            print(f'{person} disertir died in agony')

    def remove_from_enemies(self, person):
        target_index = self.enemies.index(person)
        self.enemies.pop(target_index)
        


class Enemy:
    def __init__(self, name, surname, *args, **kwargs):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'


class Animations:
    def __init__(self, *args, **kwargs):
        self.base_animation_time = kwargs.get('animation_time', 30)

    @staticmethod
    def animated_dots():
        it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
        for x in range(30):
            time.sleep(.3)
            print(next(it), end='', flush=True)
        print('\n')

if __name__ == '__main__':
    stalin = Stalin()
    stalin.repressions()
