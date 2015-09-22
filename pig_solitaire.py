class Dice:

    def roll(self):
        roll = random.randint(1,6)
        return roll


class Opponent:

    def __init__(self):
        self.dice = Dice()
        self.score = 0
        self.total_score = 0

    def roll(self):
        return self.dice.roll()

    def round_score(self):
        roll = self.roll()
        if roll > 1:
            self.score += roll
        else:
            self.score = 0
        return self.score

    def roll_or_hold(self):
        response = input("Do you want to roll or hold? (Roll/Hold)".lower())
        if response == 'hold':
            self.total_score += self.score
            return self.total_score
        if response == 'roll':
            self.round_score()
            print(self.score)
            return self.roll_or_hold()
