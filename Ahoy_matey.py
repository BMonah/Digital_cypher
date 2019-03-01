class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        self.booty_units = None

    def is_worth_it(self):
        self.booty_units = self.draft - self.crew*1.5
        return True if self.booty_units > 20 else False
