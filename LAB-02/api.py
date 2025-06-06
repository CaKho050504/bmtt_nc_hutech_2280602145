from cipher.caesar import CaesarCipher
from flask import Flask, request, jsonify

app = Flask(__name__)

caesar_cipher = CaesarCipher()

#@app.route("/api/playfair/creatematrix", methods =["POST"])
#def playfair_creatematrix():
#   data = request.json
#  key = data['key']
# playfair_matrix = playfair_cipher.create_playfair_matrix(key)
#return jsonify({'playfair_matrix': playfair_matrix})

@app.route("/api/caesar/encrypt", methods =["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_message = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_message})

@app.route("/api/caesar/decrypt", methods =["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_message = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)