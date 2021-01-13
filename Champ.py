from Sportsman import Sportsman

class Champ(Sportsman):
    def run(self, distance = None):
        if type(distance) == int or type(distance) == float:
            if distance == 60:
                res = 5.1
                return res
            if distance == 100:
                res = 10.2
                return res
        return False
    def jump(self, type_jump = None):
        if type(type_jump) == str:
            if type_jump == "from the spot":
                res = 5.5
                return  res
            if type_jump == "with a running start":
                res = 12
                return  res
        return False
    def programming(self, code = None):
        if type(code) == str:
            if code == "Govnokod":
                res = True
                return res
            if code == "normal'niy cod":
                res = False
                return  res
        return False

