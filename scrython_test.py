import scrython
#   https://github.com/NandaScott/Scrython/tree/master/docs

test = scrython.Code(code="clb")

print(test.card_count())

rarity = 'm'

test2 = scrython.sets.Sets()

for set in test2.data():
    if set.get('code') == 'lea':
        print('it works!')


