from attack_card_generator import getAttackCardsStack
from dodge_card_generator import getDodgeCardsStack
import json

attack_stack = getAttackCardsStack(20)
dodge_stack = getDodgeCardsStack(20)

index = 1
tabs_number = 1
js = '{ "Cards" : { '
for card in attack_stack:
    temp = '"Card' + str(index) + '" : '
    js += "" + temp + "{"
    js += '"Damage" : "' + str(card.damage) + '",'
    js += '"Bullets" : "' + str(card.bullets) + '",'
    js += '"Accuracy_Penalty" : "' + str(card.accuracy_penalty) + '"'
    js += "},"
    index += 1
index = 1
for card in dodge_stack:
    temp = '"Card' + str(index) + '" : '
    js += "" + temp + "{"
    js += '"Steps" : "' + str(card.steps) + '",'
    js += '"Accuracy" : "' + str(card.accuracy) + '"'
    js += "},"
    index += 1
js += '"None" : "None"'
js += '}}'
parsed = json.loads(js)
with open('Cards.json', 'w') as outfile:
    json.dump(parsed, outfile)
