

import random


damage_range = range(0, 25)
bullets_range = range(0, 6)
accuracy_penalty_range = range(0, 90, 10)


class AttackCard:
    damage = 0
    bullets = 0
    accuracy_penalty = 0
    # TODO: Add Initiative + additional effects fields

    def __init__(self, damage, bullets, accuracy_penalty):
        """Constructor"""
        self.damage = damage
        self.bullets = bullets
        self.accuracy_penalty = accuracy_penalty


def getAttackCardsStack(n):
    attackCards = []
    for i in range(0, n):
        generateAttackCard()


def generateAttackCard():
    damage = random.randint(damage_range.start, damage_range.stop)
    print(damage)

getAttackCardsStack(10)
