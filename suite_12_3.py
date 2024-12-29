class Runner:
    def __init__(self, name, distance = 0, is_frozen = False):
        self.name = name
        self.distance = distance
        self.is_frozen = is_frozen

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class Tournament:
    def __init__(self, distance, *participants, is_frozen = True):
        self.full_distance = distance
        self.participants = list(participants)
        self.is_frozen = is_frozen

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers