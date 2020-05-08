class Enigma:
    def __init__(self, rotors, plugboard, reflector):
        self.rotors = rotors
        self.plugboard = plugboard
        self.reflector = reflector

    def encrypt(self, text: str):
        data = text.upper().replace(" ", "")
        string = ""
        for char in data:
            string += self.step(char, True)
        return string

    def decrypt(self, text: str):
        data = text.upper().replace(" ", "")
        string = ""
        for char in data:
            string += self.step(char, False)
        return string

    def step(self, char: chr, flag: bool):
        is_turnover = self.rotors[0].step()
        if is_turnover:
            is_turnover = self.rotors[1].step()
            if is_turnover:
                self.rotors[2].step()

        output = self.plugboard.get(char)

        for rotor in self.rotors:
            output = rotor.scramble(output) if flag else rotor.unscramble(output)

        output = self.reflector.get(output)

        for rotor in self.rotors[::-1]:
            output = rotor.scramble(output) if flag else rotor.unscramble(output)

        output = self.plugboard.get(output)

        return output
