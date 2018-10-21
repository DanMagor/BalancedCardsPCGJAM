import random

parameters = {'STEPS': 0, 'ACCURACY': 0}

steps_range_min = 1
steps_range_max = 5
accuracy_range_min = 10
accuracy_range_max = 100
accuracy_range_step = 10
max_card_cost = 2
card_cost = 0

minimal_expected_dodge = 1
maximal_expected_dodge = 4

class DodgeCard:
    steps = 0
    accuracy = 0

    # TODO: Add Initiative + additional effects fields

    def __init__(self, steps = 0, accuracy = 0):
        """Constructor"""
        self.steps = steps
        self.accuracy = accuracy


def getDodgeCardsStack(n):
    dodge_cards_stack = []
    for i in range(0, n):
        card = generateDodgeCard()
        while calculateCardFitness(card) < minimal_expected_dodge or calculateCardFitness(card) > maximal_expected_dodge:
            card = generateDodgeCard()
        dodge_cards_stack.append(card)
    return dodge_cards_stack

def calculateCardFitness(card):
    #TODO: Add2 patameters
    fitness = card.steps * ((100 - card.accuracy) / 100)
    return fitness

def generateDodgeCard():
    steps = (random.randint(steps_range_min, steps_range_max) - steps_range_min) / \
             (steps_range_max - steps_range_min)
    accuracy = (random.randrange(accuracy_range_min, accuracy_range_max, accuracy_range_step)
             - accuracy_range_min) / (accuracy_range_max - accuracy_range_min)

    # TODO: Add 2 other parameters

    # write random generated and normalized parameters
    parameters["STEPS"] = steps
    parameters["ACCURACY"] = accuracy

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

    steps = round(parameters["STEPS"] * (steps_range_max - steps_range_min) + steps_range_min)
    accuracy = round(parameters["ACCURACY"] * (accuracy_range_max - accuracy_range_min) + accuracy_range_min, -1)

    # TODO ADD 2 parameters

    card = DodgeCard(steps=steps, accuracy=accuracy)

    return card


getDodgeCardsStack(10)
