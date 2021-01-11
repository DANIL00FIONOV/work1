from Sportsman import Sportsman

class Champ(Sportsman):
    def run(self, distance):
        if type(distance) == int:
            if distance == 60:
                res = 5
                return res
            if distance == 100:
                res = 10
                return res
        return False
    def jump(self, type_jump):
        if type(type_jump) == str:
            if type_jump == "from the spot":
                res = 5
                return  res
            if type_jump == "with a running start":
                res = 12
                return  res
        return False


