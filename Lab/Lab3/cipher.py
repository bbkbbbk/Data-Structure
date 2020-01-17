import random

class SubtitutionCipher:
    def __init__(self, string):
        self.encoder_key = {chr(65 + i) : string[i] for i in range(len(string))}
        self.decoder_key = {value : key for key, value in self.encoder_key.items()}

    def encrypt(self, string):
        encrypted = ''
        for s in string:
            encrypted += self.encoder_key[s]
        return encrypted

    def decrypt(self, string):
        decrypted = ''
        for s in string:
            decrypted += self.decoder_key[s]
        return decrypted

class CaesarCipher(SubtitutionCipher):
    def __init__(self, key):
        upper = []
        for i in range(26):
            if i + 65 + key <= 90:
                upper.append(chr(i + 65 + key))
            else:
                upper.append(chr((i + 65 + key) % 90 + 64))
        super().__init__(''.join(upper))

class RandomCipher(SubtitutionCipher):
    def __init__(self):
        string = random.sample(range(65, 91), 26)
        string = [chr(i) for i in string]
        super().__init__(string)


s = SubtitutionCipher('MRZULWXEJBOSNHIKTCGVQPFYAD')
print(s.encoder_key)
print(s.encrypt('ABC'))
print(s.decrypt('ABC'))

c = CaesarCipher(5)
print(c.encoder_key)
print(c.encrypt('ABC'))
print(c.decrypt('ABC'))

r = RandomCipher()
print(r.encoder_key)
print(r.encrypt('ABC'))
print(r.decrypt('ABC'))