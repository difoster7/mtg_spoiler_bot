from requests import get
from json import loads

# status codes
# 200 = success
# 404 = NOT FOUND

search_query = 'Vindicate'

cards = loads(get(f"https://api.scryfall.com/cards/search?q=set=CLB").text)

print(cards)

