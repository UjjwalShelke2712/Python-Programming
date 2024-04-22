# C1-84158-Ujjwal Shelke


class Painting:
    def __init__(self):
        self.painting_cost = 0

    def calculatePaintingCost(self):
        return self.painting_cost


class FlatPainting(Painting):
    def __init__(self, noOfRooms):
        Painting.__init__(self)
        self.noOfRooms = noOfRooms
        self.painting_cost = 10000 * self.noOfRooms

    def calculatePaintingCost(self):
        return self.painting_cost


class BuildingPainting(Painting):
    def __init__(self, noOfFlats):
        Painting.__init__(self)
        self.noOfFlats = noOfFlats
        self.painting_cost = 25000 * self.noOfFlats

    def calculatePaintingCost(self):
        return self.painting_cost


flat = FlatPainting(3)
print("Flat painting cost: ", flat.calculatePaintingCost())

building = BuildingPainting(5)
print("Building painting cost: ", building.calculatePaintingCost())
