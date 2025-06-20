class PlayfairCipher:
    def __init__(self, key=None):
        self.table = None
        if key is not None:
            self.create_table(key)

    def create_table(self, key):
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        table = []
        key = ''.join(sorted(set(key), key=key.index))
        for char in key:
            if char in alphabet:
                alphabet = alphabet.replace(char, '')
        key += alphabet
        key = key.replace('J', 'I')
        table = [list(key[i:i+5]) for i in range(0, 25, 5)]
        self.table = table

    def prepare_text(self, text):
        text = text.upper().replace('J', 'I')
        text = ''.join(filter(str.isalpha, text))
        text = text.replace(' ', '')
        if len(text) % 2 == 1:
            text += 'X'
        return text

    def find_position(self, char):
        for i in range(5):
            for j in range(5):
                if self.table[i][j] == char:
                    return (i, j)

    def encrypt(self, plain_text, key):
        self.create_table(key)
        plain_text = self.prepare_text(plain_text)
        cipher_text = ''
        for i in range(0, len(plain_text), 2):
            char1 = plain_text[i]
            char2 = plain_text[i+1]
            pos1 = self.find_position(char1)
            pos2 = self.find_position(char2)
            if pos1[0] == pos2[0]:
                cipher_text += self.table[pos1[0]][(pos1[1] + 1) % 5] + self.table[pos2[0]][(pos2[1] + 1) % 5]
            elif pos1[1] == pos2[1]:
                cipher_text += self.table[(pos1[0] + 1) % 5][pos1[1]] + self.table[(pos2[0] + 1) % 5][pos2[1]]
            else:
                cipher_text += self.table[pos1[0]][pos2[1]] + self.table[pos2[0]][pos1[1]]
        return cipher_text

    def decrypt(self, cipher_text, key):
        self.create_table(key)
        cipher_text = self.prepare_text(cipher_text)
        orig_text = ''
        for i in range(0, len(cipher_text), 2):
            char1 = cipher_text[i]
            char2 = cipher_text[i+1]
            pos1 = self.find_position(char1)
            pos2 = self.find_position(char2)
            if pos1[0] == pos2[0]:
                orig_text += self.table[pos1[0]][(pos1[1] - 1) % 5] + self.table[pos2[0]][(pos2[1] - 1) % 5]
            elif pos1[1] == pos2[1]:
                orig_text += self.table[(pos1[0] - 1) % 5][pos1[1]] + self.table[(pos2[0] - 1) % 5][pos2[1]]
            else:
                orig_text += self.table[pos1[0]][pos2[1]] + self.table[pos2[0]][pos1[1]]
        return orig_text
