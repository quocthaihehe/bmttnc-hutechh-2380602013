# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CaesarCipher(object):
    def setupUi(self, CaesarCipher):
        CaesarCipher.setObjectName("CaesarCipher")
        CaesarCipher.resize(573, 424)
        self.centralwidget = QtWidgets.QWidget(CaesarCipher)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 71, 21))
        self.label.setObjectName("label")
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(130, 60, 401, 91))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.txt_key = QtWidgets.QLineEdit(self.centralwidget)  # ✅ Đổi sang QLineEdit
        self.txt_key.setGeometry(QtCore.QRect(130, 170, 401, 31))
        self.txt_key.setObjectName("txt_key")
        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(130, 220, 401, 111))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 10, 191, 41))
        self.label_4.setObjectName("label_4")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(310, 350, 91, 31))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(450, 350, 81, 31))
        self.btn_decrypt.setObjectName("btn_decrypt")
        CaesarCipher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CaesarCipher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 21))
        self.menubar.setObjectName("menubar")
        CaesarCipher.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CaesarCipher)
        self.statusbar.setObjectName("statusbar")
        CaesarCipher.setStatusBar(self.statusbar)

        self.retranslateUi(CaesarCipher)
        QtCore.QMetaObject.connectSlotsByName(CaesarCipher)

    def retranslateUi(self, CaesarCipher):
        _translate = QtCore.QCoreApplication.translate
        CaesarCipher.setWindowTitle(_translate("CaesarCipher", "CaesarCipher"))
        self.label.setText(_translate("CaesarCipher", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Plaintext:</span></p></body></html>"))
        self.label_2.setText(_translate("CaesarCipher", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Key:</span></p></body></html>"))
        self.label_3.setText(_translate("CaesarCipher", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ciphertext:</span></p></body></html>"))
        self.label_4.setText(_translate("CaesarCipher", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">CAESAR CIPHER</span></p></body></html>"))
        self.btn_encrypt.setText(_translate("CaesarCipher", "Encrypt"))
        self.btn_decrypt.setText(_translate("CaesarCipher", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaesarCipher = QtWidgets.QMainWindow()
    ui = Ui_CaesarCipher()
    ui.setupUi(CaesarCipher)
    CaesarCipher.show()
    sys.exit(app.exec_())