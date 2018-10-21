import random

parameters = {'DAMAGE': 0, 'BULLETS': 0, 'ACCURACY_PENALTY': 0}

damage_range_min = 0
damage_range_max = 15
bullets_range_min = 1
bullets_range_max = 6
accuracy_penalty_range_min = 0
accuracy_penalty_range_max = 90
accuracy_penalty_range_step = 10
max_card_cost = 3
card_cost = 0

minimal_damage = 8


class AttackCard:
    damage = 0
    bullets = 0
    accuracy_penalty = 0

    # TODO: Add Initiative + additional effects fields

    def __init__(self, damage=0, bullets=0, accuracy_penalty=0):
        """Constructor"""
        self.damage = damage
        self.bullets = bullets
        self.accuracy_penalty = accuracy_penalty


def getAttackCardsStack(n):
    attack_cards_stack = []
    for i in range(0, n):
        card = generateAttackCard()
        while calculateCardFitness(card) < minimal_damage:
            card = generateAttackCard()
        attack_cards_stack.append(card)
    return attack_cards_stack


def calculateCardFitness(card):
    #TODO: Add2 patameters
    fitness = card.bullets*(card.damage*(100-card.accuracy_penalty)/100)
    return fitness

def generateAttackCard():
    damage = (random.randint(damage_range_min, damage_range_max) - damage_range_min) / \
             (damage_range_max - damage_range_min)
    bullets = (random.randint(bullets_range_min, bullets_range_max) - bullets_range_min) / \
              (bullets_range_max - bullets_range_min)
    accuracy_penalty = (random.randrange(accuracy_penalty_range_min, accuracy_penalty_range_max,
                                         accuracy_penalty_range_step)
                        - accuracy_penalty_range_min) / (accuracy_penalty_range_max - accuracy_penalty_range_min)

    # TODO: Add 2 other parameters

    # write random generated and normalized parameters
    parameters["DAMAGE"] = damage
    parameters["BULLETS"] = bullets
    parameters["ACCURACY_PENALTY"] = accuracy_penalty

    parameters_copy = parameters.copy()
    rand_parameter = random.choice(list(parameters_copy.keys()))
    k1 = parameters_copy[rand_parameter]
    card_cost = k1
    parameters[rand_parameter] = k1
    parameters_copy.pop(rand_parameter)

    while parameters_copy:
        rand_parameter = random.choice(list(parameters_copy.keys()))
        c = 1 - card_cost / max_card_cost
        k = c * parameters_copy[rand_parameter]
        card_cost += k
        parameters[rand_parameter] = k
        parameters_copy.pop(rand_parameter)

    damage = round(parameters["DAMAGE"] * (damage_range_max - damage_range_min) + damage_range_min)
    bullets = round(parameters["BULLETS"] * (bullets_range_max - damage_range_min) + damage_range_min)
    accuracy_penalty = round(parameters["ACCURACY_PENALTY"] * (accuracy_penalty_range_max
                                                               - accuracy_penalty_range_min) +
                             accuracy_penalty_range_min, -1)
    accuracy_penalty = 100 - accuracy_penalty
    if accuracy_penalty < 0:
        accuracy_penalty = 0

    if bullets == 0:
        bullets = 1

    # TODO ADD 2 parameters

    card = AttackCard(damage=damage, bullets=bullets, accuracy_penalty=accuracy_penalty)

    return card


getAttackCardsStack(10)
