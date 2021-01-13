class Sportsman:
    def __init__(self):
        self.steroids = "steroids"

    def run(self, distance = None):
        if type(distance) == int or type(distance) == float:
            if distance == 60:
                res = 7.1
                return res
            if distance == 100:
                res = 12.8
                return res
        return False
    def jump(self, type_jump = None):
        if type(type_jump) == str :
            if type_jump == "from the spot":
                res = 3
                return  res
            if type_jump == "with a running start":
                res = 8
                return  res
        return False
    def sleep(self, hours = None):
        if type(hours) == int or type(hours) == float:
            if hours >= 8 or hours <= 10:
                res = True
                return  res
            if hours >= 0 or hours <= 8:
                res = False
                return  res
        return False
    def eat(self, meal = None):
        if meal == self.steroids:
            res = True
            return res
        return False






