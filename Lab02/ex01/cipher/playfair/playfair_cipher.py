class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        if not key or not any(c.isalpha() for c in key):
            raise ValueError("Khóa bắt buộc phải chứa ít nhất một chữ cái.")
            
        key = key.upper().replace("J", "I")
        key = ''.join(filter(str.isalpha, key))
        
        matrix_list = []
        for char in key:
            if char not in matrix_list:
                matrix_list.append(char)
                
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in matrix_list:
                matrix_list.append(char)
                
        playfair_matrix = [matrix_list[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def preprocess_text(self, text):
        if not text or not any(c.isalpha() for c in text):
            raise ValueError("Bản rõ bắt buộc phải chứa ít nhất một chữ cái.")
            
        text = text.upper().replace("J", "I")
        text = ''.join(filter(str.isalpha, text))
        
        processed_text = ""
        i = 0
        while i < len(text):
            processed_text += text[i]
            if i + 1 < len(text):
                if text[i] == text[i+1]:
                    processed_text += 'X'
                else:
                    processed_text += text[i+1]
                    i += 1
            i += 1
            
        if len(processed_text) % 2 != 0:
            processed_text += 'X'
            
        return processed_text

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        raise ValueError(f"Letter {letter} not found in matrix.")

    def playfair_encrypt(self, plain_text, key):
        matrix = self.create_playfair_matrix(key)
        processed_text = self.preprocess_text(plain_text)
        encrypted_text = ""

        for i in range(0, len(processed_text), 2):
            row1, col1 = self.find_letter_coords(matrix, processed_text[i])
            row2, col2 = self.find_letter_coords(matrix, processed_text[i+1])

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, key):
        if not cipher_text or not any(c.isalpha() for c in cipher_text):
            raise ValueError("Cipher text must contain letters.")
            
        cipher_text = cipher_text.upper().replace("J", "I")
        cipher_text = ''.join(filter(str.isalpha, cipher_text))
        
        if len(cipher_text) % 2 != 0:
            raise ValueError("Cipher text length must be even.")

        matrix = self.create_playfair_matrix(key)
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            row1, col1 = self.find_letter_coords(matrix, cipher_text[i])
            row2, col2 = self.find_letter_coords(matrix, cipher_text[i+1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return decrypted_text