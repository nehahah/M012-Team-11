import random


class Cafe():
    def __init__(self, average_happiness, standard_deviation):
        self.avg_hpp = average_happiness
        self.std_dev = standard_deviation
        self.visit_history = []

    def visit(self) -> float:
        happiness = random.normalvariate(self.avg_hpp, self.std_dev)
        self.visit_history.append(happiness)
        return happiness