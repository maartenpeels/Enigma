import json

rf_types = json.load(open("./data/reflectors.json", mode="r"))


class Reflector:
    def __init__(self, type="A"):
        self.reflector = rf_types.get(type)

    def get(self, char):
        return self.reflector.get(char)
