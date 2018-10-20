import random
from enum import Enum

class AttackProperty(Enum):
    damage = 1
    bullets = 2
    accuracy_penalty = 3


damage_range_min = 0
damage_range_max = 25
bullets_range_min = 0
bullets_range_max = 6
accuracy_penalty_range_min = 0
accuracy_penalty_range_max = 90
accuracy_penalty_range_step = 10


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

    damage = random.randint(damage_range_min, damage_range_max)
    print(damage)


getAttackCardsStack(10)
