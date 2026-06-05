from flask import Flask, render_template, request
from ex01.cipher.caesar.caesar_cipher import CaesarCipher
from ex01.cipher.vigenere.vigenere_cipher import VigenereCipher
from ex01.cipher.railfence.railfence_cipher import RailFenceCipher
from ex01.cipher.playfair.playfair_cipher import PlayFairCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputKeyPlain'])
        Caesar = CaesarCipher()
        encrypted_text = Caesar.encrypt_text(text, key)
        return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
    except ValueError as e:
        return f"<h3>LỖI RÀNG BUỘC:</h3> <p style='color:red;'>{str(e)}</p>"
    except Exception as e:
        return f"<h3>LỖI HỆ THỐNG:</h3> <p style='color:red;'>{str(e)}</p>"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputKeyCipher'])
        Caesar = CaesarCipher()
        decrypted_text = Caesar.decrypt_text(text, key)
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
    except ValueError as e:
        return f"<h3>LỖI RÀNG BUỘC:</h3> <p style='color:red;'>{str(e)}</p>"
    except Exception as e:
        return f"<h3>LỖI HỆ THỐNG:</h3> <p style='color:red;'>{str(e)}</p>"

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    try:
        text = request.form['inputPlainText']
        key = request.form['inputKeyPlain']
        Vigenere = VigenereCipher()
        encrypted_text = Vigenere.vigenere_encrypt(text, key)
        return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
    except ValueError as e:
        return f"<h3>LỖI RÀNG BUỘC:</h3> <p style='color:red;'>{str(e)}</p>"
    except Exception as e:
        return f"<h3>LỖI HỆ THỐNG:</h3> <p style='color:red;'>{str(e)}</p>"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    try:
        text = request.form['inputCipherText']
        key = request.form['inputKeyCipher']
        Vigenere = VigenereCipher()
        decrypted_text = Vigenere.vigenere_decrypt(text, key)
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
    except ValueError as e:
        return f"<h3>LỖI RÀNG BUỘC:</h3> <p style='color:red;'>{str(e)}</p>"
    except Exception as e:
        return f"<h3>LỖI HỆ THỐNG:</h3> <p style='color:red;'>{str(e)}</p>"

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputKeyPlain'])
        RailFence = RailFenceCipher()
        encrypted_text = RailFence.rail_fence_encrypt(text, key)
        return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
    except ValueError as e:
        return f"<h3>LỖI RÀNG BUỘC:</h3> <p style='color:red;'>{str(e)}</p>"
    except Exception as e:
        return f"<h3>LỖI HỆ THỐNG:</h3> <p style='color:red;'>{str(e)}</p>"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputKeyCipher'])
        RailFence = RailFenceCipher()
        decrypted_text = RailFence.rail_fence_decrypt(text, key)
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
    except ValueError as e:
        return f"<h3>LỖI RÀNG BUỘC:</h3> <p style='color:red;'>{str(e)}</p>"
    except Exception as e:
        return f"<h3>LỖI HỆ THỐNG:</h3> <p style='color:red;'>{str(e)}</p>"

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    try:
        text = request.form['inputPlainText']
        key = request.form['inputKeyPlain']
        PlayFair = PlayFairCipher()
        encrypted_text = PlayFair.playfair_encrypt(text, key)
        return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
    except ValueError as e:
        return f"<h3>LỖI RÀNG BUỘC:</h3> <p style='color:red;'>{str(e)}</p>"
    except Exception as e:
        return f"<h3>LỖI HỆ THỐNG:</h3> <p style='color:red;'>{str(e)}</p>"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    try:
        text = request.form['inputCipherText']
        key = request.form['inputKeyCipher']
        PlayFair = PlayFairCipher()
        decrypted_text = PlayFair.playfair_decrypt(text, key)
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
    except ValueError as e:
        return f"<h3>LỖI RÀNG BUỘC:</h3> <p style='color:red;'>{str(e)}</p>"
    except Exception as e:
        return f"<h3>LỖI HỆ THỐNG:</h3> <p style='color:red;'>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)