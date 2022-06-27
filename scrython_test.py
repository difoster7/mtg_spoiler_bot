import scrython
#   https://github.com/NandaScott/Scrython/tree/master/docs

test = scrython.Code(code="clb")

print(test.card_count())

rarity = 'm'

test2 = scrython.cards.Search(q=f"set=stx, r>={rarity}")

cards = test2.data()

for card in cards:
    print(card['name'])