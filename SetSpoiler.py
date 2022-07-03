from Rarity import Rarity
from datetime import datetime
import scrython


class SetSpoiler:
    '''Tracks card spoilers for a magic set on Scryfall'''

    def __init__(self, set_code='999', spoiler_level=Rarity.Rarity.RARE):
        assert (len(set_code) == 3, 'Invalid set code. Set codes must be exactly three characters')

        exists = 0
        for set in scrython.sets.Sets().data:
            if set_code == set.get('code'):
                exists = 1
        if exists:
            self.set_code = set_code

        self.spoiler_level = spoiler_level
        self.spoilers_start = datetime.now()


    def update_spoilers(self):
        pass    #TODO


    def print_spoilers(self):
        pass #TODO


    def start_spoilers(self):
        pass    #TODO


    def pause_spoilers(self):
        pass    #TODO


    def stop_spoilers(self):
        pass    #TODO


    def __str__(self):
        return self.set_code    #TODO