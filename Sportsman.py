class Sportsman:
    def __init__(self):
        self.steroids = "steroids"

    def run(self, distance):
        if type(distance) == int:
            if distance == 60:
                res = 7
                return res
            if distance == 100:
                res = 12
                return res
        return False
    def jump(self, type_jump):
        if type(type_jump) == str:
            if type_jump == "from the spot":
                res = 3
                return  res
            if type_jump == "with a running start":
                res = 8
                return  res
        return False
    def sleep(self, hours):
        if type(hours) == int:
            if hours >= 8 or hours <= 10:
                res = "I recovered"
                return  res
            if hours >= 0 or hours <= 8:
                res = "I didn't recover"
                return  res
        return False
    def eat(self, meal):
        if meal == self.steroids:
            res = "zaebumba"
            return res
        return False






