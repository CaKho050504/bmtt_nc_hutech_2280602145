class VigenereCipher:
    def __init__(self):
        pass

    def generate_key(self, text, key):
        key = list(key)
        if len(text) == len(key):
            return ''.join(key)
        else:
            for i in range(len(text) - len(key)):
                key.append(key[i % len(key)])
        return ''.join(key)

    def encrypt(self, plain_text, key):
        plain_text = plain_text.upper()
        key = self.generate_key(plain_text, key.upper())
        cipher_text = ''

        for p, k in zip(plain_text, key):
            if p.isalpha():
                c = chr((ord(p) - ord('A') + ord(k) - ord('A')) % 26 + ord('A'))
                cipher_text += c
            else:
                cipher_text += p  

        return cipher_text

    def decrypt(self, cipher_text, key):
        # Generate key based on the length of the cipher_text
        generated_key = self.generate_key(cipher_text, key.upper())
        orig_text = ''

        for c, k in zip(cipher_text, generated_key):
            if c.isalpha():
                p = chr((ord(c) - ord('A') - (ord(k) - ord('A')) + 26) % 26 + ord('A'))
                orig_text += p
            else:
                orig_text += c

        return orig_text