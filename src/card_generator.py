from attack_card_generator import getAttackCardsStack
import json

attack_stack = getAttackCardsStack(20)

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
js += '"None" : "None"'
js += '}}'
parsed = json.loads(js)
with open('Cards.json', 'w') as outfile:
    json.dump(parsed, outfile)
