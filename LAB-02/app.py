from flask import Flask, request, render_template
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher 
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()
railfence_cipher = RailFenceCipher() 
vigenere_cipher = VigenereCipher()  
playfair_cipher = PlayfairCipher()
transposition_cipher = TranspositionCipher()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/caesar", methods=['GET', 'POST'])
def caesar():
    if request.method == 'GET':
        return render_template("caesar.html")
    elif request.method == 'POST':
        if 'encrypt' in request.form:
            plain_text = request.form['plain_text']
            key = int(request.form['key'])
            encrypted_text = caesar_cipher.encrypt(plain_text, key)
            return render_template("result.html", encrypted_text=encrypted_text)
        elif 'decrypt' in request.form:
            cipher_text = request.form['cipher_text']
            key = int(request.form['key'])
            decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
            return render_template("result.html", decrypted_text=decrypted_text)

@app.route("/railfence", methods=['GET', 'POST'])
def railfence():
    if request.method == 'GET':
        return render_template("railfence.html")
    elif request.method == 'POST':
        if 'encrypt' in request.form:
            plain_text = request.form['plain_text']
            key = int(request.form['key'])
            encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
            return render_template("result.html", encrypted_text=encrypted_text)
        elif 'decrypt' in request.form:
            cipher_text = request.form['cipher_text']
            key = int(request.form['key'])
            decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
            return render_template("result.html", decrypted_text=decrypted_text)


@app.route("/vigenere", methods=['GET', 'POST'])
def vigenere():
    if request.method == 'GET':
        return render_template("vigenere.html")
    elif request.method == 'POST':
        if 'encrypt' in request.form:
            plain_text = request.form['plain_text']
            key = request.form['key']
            encrypted_text = vigenere_cipher.encrypt(plain_text, key)
            return render_template("result.html", encrypted_text=encrypted_text)
        elif 'decrypt' in request.form:
            cipher_text = request.form['cipher_text']
            key = request.form['key']
            decrypted_text = vigenere_cipher.decrypt(cipher_text, key)
            return render_template("result.html", decrypted_text=decrypted_text)


@app.route("/playfair", methods=['GET', 'POST'])
def playfair():
    if request.method == 'GET':
        return render_template("playfair.html")
    elif request.method == 'POST':
        if 'encrypt' in request.form:
            plain_text = request.form['plain_text']
            key = request.form['key']
            playfair_cipher = PlayfairCipher(key)
            encrypted_text = playfair_cipher.encrypt(plain_text, key)
            return render_template("result.html", encrypted_text=encrypted_text)
        elif 'decrypt' in request.form:
            cipher_text = request.form['cipher_text']
            key = request.form['key']
            playfair_cipher = PlayfairCipher(key)
            decrypted_text = playfair_cipher.decrypt(cipher_text, key)
            return render_template("result.html", decrypted_text=decrypted_text)


@app.route("/transposition", methods=['GET', 'POST'])
def transposition():
    if request.method == 'GET':
        return render_template("transposition.html")
    elif request.method == 'POST':
        if 'encrypt' in request.form:
            plain_text = request.form['plain_text']
            key = int(request.form['key'])
            encrypted_text = transposition_cipher.transposition_encrypt(plain_text, key)
            return render_template("result.html", encrypted_text=encrypted_text)
        elif 'decrypt' in request.form:
            cipher_text = request.form['cipher_text']
            key = int(request.form['key'])
            decrypted_text = transposition_cipher.transposition_decrypt(cipher_text, key)
            return render_template("result.html", decrypted_text=decrypted_text)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)