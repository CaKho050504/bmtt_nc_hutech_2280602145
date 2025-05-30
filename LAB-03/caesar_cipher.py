import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        plain_text = self.ui.txt_plain_text.toPlainText()
        key = self.ui.txt_key.text()

        if not plain_text or not key:
            QMessageBox.warning(self, "Error", "Please enter both plain text and key!")
            return

        payload = {
            "plain_text": plain_text,
            "key": key,
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypted_message"])
                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", f"API Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Error", f"Connection Error: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        cipher_text = self.ui.txt_cipher_text.toPlainText()
        key = self.ui.txt_key.text()

        if not cipher_text or not key:
            QMessageBox.warning(self, "Error", "Please enter both cipher text and key!")
            return

        payload = {
            "cipher_text": cipher_text,
            "key": key,
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypted_message"])
                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", f"API Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Error", f"Connection Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())