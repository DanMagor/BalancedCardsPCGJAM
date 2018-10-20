import random

dictionary = {'DAMAGE': 1, 'BULLETS': 2, 'ACCURACY_PENALTY': 3}

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
    bullets = random.randint(bullets_range_min, bullets_range_max)
    accuracy_penalty = random.randint(accuracy_penalty_range_min, accuracy_penalty_range_max, accuracy_penalty_range_step)
    while (dictionary):
        rand = random.choice(dictionary)
        coefficient = 1
        dict.pop(rand)
        function += coefficient * rand


getAttackCardsStack(10)
