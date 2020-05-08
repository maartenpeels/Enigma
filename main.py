from enigma import Enigma
from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

e1 = Enigma(rotors=[
        Rotor(position=24, type="II"),
        Rotor(position=13, type="I"),
        Rotor(position=22, type="III")
    ],
    plugboard=Plugboard([
        ('A', 'M'),
        ('F', 'I'),
        ('N', 'V'),
        ('P', 'S'),
        ('T', 'U'),
        ('W', 'Z'),
    ]),
    reflector=Reflector("A")
)

e2 = Enigma(rotors=[
        Rotor(position=24, type="II"),
        Rotor(position=13, type="I"),
        Rotor(position=22, type="III")
    ],
    plugboard=Plugboard([
        ('A', 'M'),
        ('F', 'I'),
        ('N', 'V'),
        ('P', 'S'),
        ('T', 'U'),
        ('W', 'Z'),
    ]),
    reflector=Reflector("A")
)

input_string = "Hello"
print(f"Input: {input_string}")

encrypted_string = e1.encrypt(input_string)
print(f"Encrypted: {encrypted_string}")

answer_string = e2.decrypt(encrypted_string)
print(f"Answer: {answer_string}")
