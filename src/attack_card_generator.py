import random

parameters = {'DAMAGE', 'BULLETS', 'ACCURACY_PENALTY'}

damage_range_min = 0
damage_range_max = 25
bullets_range_min = 0
bullets_range_max = 6
accuracy_penalty_range_min = 0
accuracy_penalty_range_max = 90
accuracy_penalty_range_step = 10
card_cost = 0

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

def normalization():
    damage = (random.randint(damage_range_min, damage_range_max)  - damage_range_min) / \
             (damage_range_max - damage_range_min)
    bullets = (random.randint(bullets_range_min, bullets_range_max) - bullets_range_min) / \
              (bullets_range_max - bullets_range_min)
    accuracy_penalty = (random.randint(accuracy_penalty_range_min, accuracy_penalty_range_max, accuracy_penalty_range_step)
                        - accuracy_penalty_range_min) / (accuracy_penalty_range_max - accuracy_penalty_range_min)


def generateAttackCard():
    card_cost = 5 * random.choice(list(parameters))
    while (len(parameters)== 0):
        rand = random.choice(list(parameters))
        coefficient = 10 - card_cost / 5.55
        dict.pop(rand)
        card_cost += coefficient * rand

getAttackCardsStack(10)
