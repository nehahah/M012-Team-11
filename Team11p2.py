import random

h1 = 10  # avg happiness of cafe 1
h2 = 15
h3 = 12
d1 = 8  # deviation
d2 = 6
d3 = 5
total_happiness = 0
remaining_days = 297


happiness = random.normalvariate(h1, d1)

def exploitOnly():
    x = random.normalvariate(h1, d1)
    y = random.normalvariate(h2, d2)
    z = random.normalvariate(h3, d3)
    most = max(x, y, z)
    for i in range(0, remaining_days):
        return most
    print("Total happiness generated:", sum(most))
    
