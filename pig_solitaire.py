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
        return self.score

    def roll_or_hold(self):
        response = self.decision()
        self.decision()
        if response == 'hold':
            self.total_score += self.score
            self.score = 0
            return self.total_score
        if response == 'roll':
            self.round_score()
            print(self.score)
            return self.roll_or_hold()

    def decision(self):
        if self.score > 10:
            return "hold"
        else:
            return "roll"


class Player:

    def __init__(self):
        self.dice = Dice()
        self.score = 0
        self.total_score = 0
        self.count = 0

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
        if self.count is not 0 and self.score == 0:
            response = input("Do you want to roll or hold? (Roll/Hold)".lower())
            if response == 'hold':
                print("You hold")
                self.total_score += self.score
                self.score = 0
                self.count = 0
                return self.total_score
            if response == 'roll':
                print("You roll")
                self.round_score()
                print("your score this round: ", self.score)
                print("your total score: ", self.total_score)
                self.count += 1
                return self.roll_or_hold()
        else:
            print(self.count)
            print("You bust")
            self.count = 0
            return self.total_score
