from ..caesar.alphabet import ALPHABET
class VigenereCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def vigenere_encrypt(self, plain_text, key):
        plain_text = plain_text.upper()
        key = key.upper()
        
        if not key or not key.isalpha():
            raise ValueError("Khóa bắt buộc chỉ được chứa các chữ cái (từ A đến Z).")
        
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char in self.alphabet:
                p_idx = self.alphabet.index(char)
                k_idx = self.alphabet.index(key[key_index % len(key)])
                c_idx = (p_idx + k_idx) % 26
                encrypted_text += self.alphabet[c_idx]
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text

    def vigenere_decrypt(self, cipher_text, key):
        cipher_text = cipher_text.upper()
        key = key.upper()
        
        if not key or not key.isalpha():
            raise ValueError("Khóa bắt buộc chỉ được chứa các chữ cái (từ A đến Z).")
        
        decrypted_text = ""
        key_index = 0
        for char in cipher_text:
            if char in self.alphabet:
                c_idx = self.alphabet.index(char)
                k_idx = self.alphabet.index(key[key_index % len(key)])
                p_idx = (c_idx - k_idx) % 26
                decrypted_text += self.alphabet[p_idx]
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text