class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails == 1:
            return plain_text

        rails = ['' for _ in range(num_rails)]
        rail_index = 0
        direction = 1  

        for char in plain_text:
            rails[rail_index] += char
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return ''.join(rails)

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails == 1:
            return cipher_text

        pattern = [['' for _ in range(len(cipher_text))] for _ in range(num_rails)]
        rail_index = 0
        direction = 1

        for i in range(len(cipher_text)):
            pattern[rail_index][i] = '*'
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        index = 0
        for i in range(num_rails):
            for j in range(len(cipher_text)):
                if pattern[i][j] == '*' and index < len(cipher_text):
                    pattern[i][j] = cipher_text[index]
                    index += 1

        result = ''
        rail_index = 0
        direction = 1
        for i in range(len(cipher_text)):
            result += pattern[rail_index][i]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return result
