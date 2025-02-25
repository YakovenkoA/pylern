"""from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow 

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
    
        self.setWindowTitle("Простая программа")
        self.setGeometry(300, 250, 350, 350)
        
        self.main_text = QtWidgets.QLabel(window)
        self.main_text.setText("Это базовая надпись")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()
        
        self.btn = QtWidgets.QPushButton(window)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)


def add_label(self):
    print("add")


def application():
    app = QApplication(sys.argv)
    window = Window()
    
   
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    application() """
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow 
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        # Настройка основного окна
        self.setWindowTitle("Простая программа")
        self.setGeometry(300, 250, 350, 350)  # (x, y, ширина, высота)
        
        # Создаем новую метку (label), которая будет использоваться позже
        self.new_text = QtWidgets.QLabel(self)
        self.new_text.hide()  # Скрываем ее изначально
        
        # Создаем и настраиваем основную метку
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Это базовая надпись")
        self.main_text.move(100, 100)  # Позиционируем метку
        self.main_text.adjustSize()  # Автоматически подстраиваем размер под содержимое
        
        # Создаем и настраиваем кнопку
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)  # Позиционируем кнопку
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)  # Устанавливаем фиксированную ширину
        self.btn.clicked.connect(self.add_label)  # Связываем клик с методом add_label

    def add_label(self):
        # Этот метод вызывается при нажатии на кнопку
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)  # Позиционируем новую метку
        self.new_text.adjustSize()
        self.new_text.show()  # Показываем новую надпись

def application():
    app = QApplication(sys.argv)
    window = Window()  # Создаем экземпляр нашего основного окна
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # Запускаем цикл обработки событий приложения
    
if __name__ == "__main__":
    application()  # Запускаем наше приложение