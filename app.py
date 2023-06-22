from flask import Flask, render_template, request

app = Flask(__name__)

def encrypt_message(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                index = (ord(char) - ord('a') + key) % 26
                ciphertext += chr(index + ord('a'))
            else:
                index = (ord(char) - ord('A') + key) % 26
                ciphertext += chr(index + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def decipher(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                index = (ord(char) - ord('a') - key) % 26
                plaintext += chr(index + ord('a'))
            else:
                index = (ord(char) - ord('A') - key) % 26
                plaintext += chr(index + ord('A'))
        else:
            plaintext += char
    return plaintext

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        key = int(request.form['key'])
        encrypted_message = encrypt_message(plaintext, key)
        return render_template('encrypt.html', encrypted_message=encrypted_message)
    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        ciphertext = request.form['ciphertext']
        key = int(request.form['key'])
        decrypted_message = decipher(ciphertext, key)
        return render_template('decrypt.html', decrypted_message=decrypted_message)
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)