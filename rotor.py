import json

rotors = json.load(open('./data/rotors.json', 'r'))


class Rotor:
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]

    def __init__(self, type="IC", position=0):
        self.position = position
        self.type = type
        self.letters = list(rotors.get(type))

        if position > 0:
            for _ in range(position):
                self.letters.append(self.letters.pop(0))

    def scramble(self, data):
        index = Rotor.letters.index(data)
        output = self.letters[index]
        return output

    def unscramble(self, data):
        index = self.letters.index(data)
        output = Rotor.letters[index]
        return output

    def step(self):
        if self.position < 25:
            self.position += 1
            self.letters.append(self.letters.pop(0))
        else:
            self.position = 0
            return True
        return False
