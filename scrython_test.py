import scrython
#   https://github.com/NandaScott/Scrython/tree/master/docs
from Rarity import Rarity

r = Rarity.RARE

foo = scrython.cards.Search(q=f"s=snc, r>={r.name}")


bar = [foo.data(0), foo.data(3)]

print([card for card in foo.data() if card not in bar])




