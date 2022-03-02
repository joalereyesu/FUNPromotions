class Concert:

    def __init__(self, lineup, capacity, price, areas, date, place, promo):
        self.lineup = lineup
        self.capacity = capacity
        self.price = price
        self.areas = areas
        self.date = date
        self.place = place
        self.promo = promo

    def getLineup(self):
        return self.lineup

    def getCapacity(self):
        return self.capacity

    def getPrice(self):
        return self.price

    def getAreas(self):
        return self.areas

    def getDate(self):
        return self.date

    def getPlace(self):
        return self.place

    def getPromo(self):
        return self.promo
