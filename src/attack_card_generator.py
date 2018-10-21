import random
import json

parameters = {'DAMAGE': 0, 'BULLETS': 0, 'ACCURACY_PENALTY': 0,
              "INITIATIVE_EFFECT": {"NAME": "", "VALUE": 0}}

damage_range_min = 0
damage_range_max = 15
bullets_range_min = 1
bullets_range_max = 6
accuracy_penalty_range_min = 0
accuracy_penalty_range_max = 90
accuracy_penalty_range_step = 10
max_card_cost = 3

minimal_expected_damage = 8

# load effects
initiative_effects = {}
f = open("initiative_effects")
initiative_effects = json.load(f)


class AttackCard:
    damage = 0
    bullets = 0
    accuracy_penalty = 0
    initiative_effect = {}

    # TODO: Add Initiative + additional effects fields

    def __init__(self, damage=0, bullets=0, accuracy_penalty=0, initiative_effect={}):
        """Constructor"""
        self.damage = damage
        self.bullets = bullets
        self.accuracy_penalty = accuracy_penalty
        self.initiative_effect = initiative_effect


def getAttackCardsStack(n):
    attack_cards_stack = []

    # with open("initiative_effects") as f:
    #   initiative_effects = json.load(f)

    for i in range(0, n):
        card = generateAttackCard()
        while calculateCardFitness(card) < minimal_expected_damage:
            card = generateAttackCard()
        attack_cards_stack.append(card)
    return attack_cards_stack


def calculateCardFitness(card):
    # TODO: Add 1 patameters
    fitness = card.bullets * (card.damage * (100 - card.accuracy_penalty) / 100)
    return fitness


def generateAttackCard():
    card_cost = 0

    damage = (random.randint(damage_range_min, damage_range_max) - damage_range_min) / \
             (damage_range_max - damage_range_min)
    bullets = (random.randint(bullets_range_min, bullets_range_max) - bullets_range_min) / \
              (bullets_range_max - bullets_range_min)
    accuracy_penalty = (random.randrange(accuracy_penalty_range_min, accuracy_penalty_range_max,
                                         accuracy_penalty_range_step)
                        - accuracy_penalty_range_min) / (accuracy_penalty_range_max - accuracy_penalty_range_min)
    rand_effect = random.choice(initiative_effects)
    rand_effect = dict(rand_effect)
    rand_effect = list(rand_effect.values())[0]
    if rand_effect["hasValue"]:
        eff_val_min = rand_effect["minValue"]
        eff_val_max = rand_effect["maxValue"]
       # if (eff_val_max-eff_val_min) != 0:
        #    effect_value = (random.randint(eff_val_min, eff_val_max) - eff_val_min) / \
        #               (eff_val_max - eff_val_min)
        #else:
         #   effect_value = 0
        effect_value = (random.randint(eff_val_min, eff_val_max) - eff_val_min) / \
                           (eff_val_max - eff_val_min)
    else:
        effect_value = 1

    # TODO: Add 1 other parameters

    # write random generated and normalized parameters
    parameters["DAMAGE"] = damage
    parameters["BULLETS"] = bullets
    parameters["ACCURACY_PENALTY"] = accuracy_penalty
    temp_name = rand_effect["name"]
    temp_ef = {"NAME": temp_name, "VALUE": effect_value}

    parameters["INITIATIVE_EFFECT"] = temp_ef


    parameters_copy = parameters.copy()
    rand_parameter = random.choice(list(parameters_copy.keys()))

    if rand_parameter != "INITIATIVE_EFFECT":
        k1 = parameters_copy[rand_parameter]
        card_cost = k1
        parameters[rand_parameter] = k1
        parameters_copy.pop(rand_parameter)
    elif rand_parameter == "INITIATIVE_EFFECT":
        k1 = parameters_copy[rand_parameter]["VALUE"]
        card_cost = k1
        parameters[rand_parameter]["VALUE"] = k1
        parameters_copy.pop(rand_parameter)

    while parameters_copy:
        rand_parameter = random.choice(list(parameters_copy.keys()))
        if rand_parameter != "INITIATIVE_EFFECT":
            c = 1 - card_cost / max_card_cost
            k = c * parameters_copy[rand_parameter]
            card_cost += k
            parameters[rand_parameter] = k
            parameters_copy.pop(rand_parameter)
        elif rand_parameter == "INITIATIVE_EFFECT":
            if rand_effect["hasValue"]:
                c = 1 - card_cost / max_card_cost
                k = c * parameters_copy[rand_parameter]["VALUE"]
                card_cost += k
                parameters[rand_parameter]["VALUE"] = k
                parameters_copy.pop(rand_parameter)
            else:
                k = parameters_copy[rand_parameter]["VALUE"]
                card_cost += k
                parameters[rand_parameter]["VALUE"] = k
                parameters_copy.pop(rand_parameter)

    damage = round(parameters["DAMAGE"] * (damage_range_max - damage_range_min) + damage_range_min)

    bullets = round(parameters["BULLETS"] * (bullets_range_max - damage_range_min) + damage_range_min)
    if bullets == 0:
        bullets = 1

    accuracy_penalty = round(parameters["ACCURACY_PENALTY"] * (accuracy_penalty_range_max
                                                               - accuracy_penalty_range_min) +
                             accuracy_penalty_range_min, -1)
    accuracy_penalty = 100 - accuracy_penalty

    if accuracy_penalty < 0:
        accuracy_penalty = 0

    effect_name = parameters["INITIATIVE_EFFECT"]

    effect_name = parameters["INITIATIVE_EFFECT"]["NAME"]




    if rand_effect["hasValue"]:

        effect_value = round(parameters["INITIATIVE_EFFECT"]["VALUE"] * (eff_val_max
                                                - eff_val_min) +
              eff_val_min, -1)
    else:
        effect_value = 0
    initiative_effect = {"NAME": effect_name, "VALUE": effect_value}

    # TODO ADD 1 parameters

    card = AttackCard(damage=damage, bullets=bullets, accuracy_penalty=accuracy_penalty,
                      initiative_effect=initiative_effect)

    return card
