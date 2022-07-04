from Rarity import Rarity
from datetime import datetime
import scrython


class SetSpoiler:
    '''Tracks card spoilers for a magic set on Scryfall'''

    def __init__(self, set_code='999', spoiler_level=Rarity.Rarity.RARE):

        # check for valid set code
        assert (len(set_code) == 3, 'Invalid set code. Set codes must be exactly three characters')

        # initialize variables
        self.set_code = set_code
        self.spoiler_level = spoiler_level
        self.spoilers_start = datetime.now()
        self.last_update = None
        self.spoilers = {}

        # Get list of initial spoilers
        self.update_spoilers()

    def update_spoilers(self):
        '''Update the current spoiler list'''

        # check for valid set code
        if self.update_spoilers() == '999':
            return

        # retrieve newly spoiled cards
        avail_cards = scrython.cards.Search(q=f"s={self.set_code}, r>={self.spoiler_level}").data()
        new_cards = [card for card in avail_cards if card not in self.spoilers]

        # return new cards (if any)
        if len(new_cards) > 0:
            self.last_update = datetime.now()
            self.spoilers += new_cards
            return new_cards
        else:
            return None


    def print_spoilers(self):
        pass  # TODO

    def __str__(self):
        return self.set_code  # TODO
