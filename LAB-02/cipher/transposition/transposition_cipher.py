class TranspositionCipher:
    def __init__(self):
        pass

    def transposition_encrypt(self, plain_text, key):
        # Tạo một lưới với số hàng và cột dựa trên key
        rows = len(plain_text) // key
        if len(plain_text) % key!= 0:
            rows += 1
        grid = [['' for _ in range(key)] for _ in range(rows)]

        # Đổ văn bản vào lưới theo hàng
        index = 0
        for i in range(rows):
            for j in range(key):
                if index < len(plain_text):
                    grid[i][j] = plain_text[index]
                    index += 1

        # Trộn cột để tạo ra văn bản mã hóa
        cipher_text = ''
        for j in range(key):
            for i in range(rows):
                if grid[i][j]!= '':
                    cipher_text += grid[i][j]

        return cipher_text

    def transposition_decrypt(self, cipher_text, key):
        # Tạo một lưới với số hàng và cột dựa trên key
        rows = len(cipher_text) // key
        if len(cipher_text) % key!= 0:
            rows += 1
        grid = [['' for _ in range(key)] for _ in range(rows)]

        # Đổ văn bản mã hóa vào lưới theo cột
        index = 0
        for j in range(key):
            for i in range(rows):
                if index < len(cipher_text):
                    grid[i][j] = cipher_text[index]
                    index += 1

        # Tạo lại văn bản gốc theo hàng
        plain_text = ''
        for i in range(rows):
            for j in range(key):
                if grid[i][j]!= '':
                    plain_text += grid[i][j]

        return plain_text
