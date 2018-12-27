import random
import time

from actors import Creature, Wizard, SmallAnimal, Dragon

def main():
    print_header()
    game_loop()

def print_header():
    print()
    print('-----------------------------------------------------------------------')
    print('''
       (  )   /\   _                 (
        \ |  (  \ ( \.(               )                      _____
      \  \ \  `  `   ) \             (  ___                 / _   \\
     (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
    - .-               \+  ;          (  O                           \____
         WIZARD BATTLE        )        \_____________  `              \  /
    (__       APP      +- .( -'.- <. - _  VVVVVVV VV V\                 \/
    (_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
      .    /./.+-  . .- /  +--  - .     \______________//_              \_______
      (__ ' /x  / x _/ (                                  \___'          \     /
     , x / ( '  . / .  /                                      |           \   /
        /  /  _/ /    +                                      /              \/
       '  (__/                                             /                  \\
        ''')
    print()
    print('-----------------------------------------------------------------------')


print()
def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000)
    ]
    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appeared from the dark and foggy forest')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides time to recover")
                time.sleep(5)
                print("The wizard is revitalized")
        elif cmd =='r':
            print('the wizard is unsure and runs away')
        elif cmd =='l':
            print("The wizard stops and looks around and sees")
            for c in creatures:
                print(f'* {c.name} with a level of {c.level}')
        else:
            print('bye')
            break

        if not creatures:
            print('you have defeated all the creatures')
            break


if __name__ == '__main__':
    main()