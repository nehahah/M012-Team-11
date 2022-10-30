import random
from Cafe import Cafe

# h1 = 10  # avg happiness of cafe 1
# h2 = 15
# h3 = 12
# d1 = 8  # deviation
# d2 = 6
# d3 = 5
total_happiness = 0
remaining_days = 297

cafe1, cafe2, cafe3 = Cafe(10, 8), Cafe(15, 6), Cafe(12, 5)


# happiness = random.normalvariate(h1, d1)
# happiness = cafe.visit()

def exploitOnly():
    # x = random.normalvariate(h1, d1)
    # y = random.normalvariate(h2, d2)
    # z = random.normalvariate(h3, d3)
    x = cafe1.visit()
    y = cafe2.visit()
    z = cafe3.visit()
    most = max(x, y, z)
    for i in range(0, remaining_days):
        return most
    print("Total happiness generated:", sum(most))
    
