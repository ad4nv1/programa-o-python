from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide2.QtGui import QFont, QIcon, QPixmap
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import sys

class janela(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ENVIO EASY")
        self.setGeometry(800, 100, 600, 750)
        self.setMinimumHeight(650)
        self.setMinimumWidth(600)
        self.setMaximumHeight(550)
        self.setMaximumWidth(400)
        self.setToolTip("envio rapidão")

        self.add_imagem()

    def add_imagem(self):
        imagem1 = QIcon("iconefundo")
        label1 = QLabel("nome", self)
        pixmap1 = imagem1.pixmap(100, 100, QIcon.Active)
        

        label1.setPixmap(pixmap1)

        imagem2 = QIcon("ifpeplt")
        label2 = QLabel("nome", self)
        pixmap2 = imagem2.pixmap(800, 790, QIcon.Active)
        label2.move(250, 100)
        

        label2.setPixmap(pixmap2)

        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: darkred")

        iconeapp = QIcon("icone1")
        self.setWindowIcon(iconeapp)


        self.montar_formulario()

        self.add_butao()



    def montar_formulario(self):
        global campo1, campo2, campo3, campo4, campo5
        
        fonte = QFont('fontes/letraas')
        fonte.setPointSize(17)

        lbl_nome = QLabel('ENVIAR EMAIL', self)
        lbl_nome.move(110, 30)
        lbl_nome.setFont(fonte)


        campo1 = QLineEdit(self)
        campo1.move(65, 80)
        campo1.setFont(fonte)
        campo1.setPlaceholderText('Digite seu Email')
        campo1.setFont(fonte)
        campo1.setStyleSheet('background-color: darkgray')

        campo2 = QLineEdit(self)
        campo2.move(65, 120)
        campo2.setFont(fonte)
        campo2.setPlaceholderText('Digite sua senha')
        campo2.setEchoMode(QLineEdit.EchoMode.Password)
        campo2.setStyleSheet('background-color: darkgray')

        campo3 = QLineEdit(self)
        campo3.move(65, 200)
        campo3.setFont(fonte)
        campo3.setPlaceholderText('mensagem')
        campo3.setGeometry(65, 200, 257, 200)
        campo3.setFont(fonte)
        campo3.setStyleSheet('background-color: white')

        campo4 = QLineEdit(self)
        campo4.move(65, 160)
        campo4.setFont(fonte)
        campo4.setPlaceholderText('titulo do email')
        campo4.setFont(fonte)
        campo4.setStyleSheet('background-color: white')

        campo5 = QLineEdit(self)
        campo5.move(65, 400)
        campo5.setFont(fonte)
        campo5.setPlaceholderText('Para')
        campo5.setFont(fonte)
        campo5.setStyleSheet('background-color: darkgray')



    def add_butao(self):
        butao1 = QPushButton('ENVIAR', self)
        butao1.move(145, 500)
        butao1.clicked.connect(self.acao_butao)
        butao1.setStyleSheet('background-color: white')




    def acao_butao(self):
        msg = MIMEMultipart()
        message = campo3.text()
        password = campo2.text()
        msg['From'] = campo1.text()
        msg['To'] = campo5.text()
        msg['Subject'] = campo4.text()
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        info1 = QMessageBox.question(self, "ENVIADA",
        "Mensagem enviada com sucesso! deseja sair?",
         QMessageBox.Yes | QMessageBox.No)

        if info1 == QMessageBox.Yes:
            janela.hide(self)

    



myApp = QApplication(sys.argv)

jane = janela()
jane.show()
myApp.exec_()
sys.exit(0)