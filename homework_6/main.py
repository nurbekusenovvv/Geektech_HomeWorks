from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys 
import random


class RandomWindow(QMainWindow):
    def __init__(self):
        super(RandomWindow, self).__init__()
        self.game_balance = 60
        loadUi('random.ui', self)
        self.start.clicked.connect(self.start_game)
        
    def __generate_random_number(self):
        return random.randint(1, 10)
        
    def start_game(self):
        print("Start Game")
        # self.game_balance -= 20
        self.balance.setText(f"Balance:{self.game_balance}с")
        self.get_random_number = self.__generate_random_number()
        if self.get_random_number == 1:
            self.one.clicked.connect(lambda: self.one_button(self.get_random_number))
        elif self.get_random_number == 2:
            self.two.clicked.connect(lambda: self.two_button(self.get_random_number))
        elif self.get_random_number == 3:
            self.three.clicked.connect(lambda: self.three_button(self.get_random_number))
        elif self.get_random_number == 4:
            self.four.clicked.connect(lambda: self.four_button(self.get_random_number))
        elif self.get_random_number == 5:
            self.five.clicked.connect(lambda: self.five_button(self.get_random_number))
        elif self.get_random_number == 6:
            self.six.clicked.connect(lambda: self.six_button(self.get_random_number))
        elif self.get_random_number == 7:
            self.seven.clicked.connect(lambda: self.seven_button(self.get_random_number))
        elif self.get_random_number == 8:
            self.eight.clicked.connect(lambda: self.eight_button(self.get_random_number))
        elif self.get_random_number == 9:
            self.nine.clicked.connect(lambda: self.nine_button(self.get_random_number))
        elif self.get_random_number == 10:
            self.ten.clicked.connect(lambda: self.ten_button(self.get_random_number))
        
        
        print(self.get_random_number)
        
            
    def one_button(self, random_number):
        num1 = int(self.one.text())
        if num1 == random_number:
            self.game_balance += 80
            self.balance.setText(f"Balance:{self.game_balance}с")
            self.attemps.setText(f"Win")
            self.start_game()
            self.get_random_number = self.__generate_random_number()

    def two_button(self, random_number):
        num2 = int(self.two.text())
        if num2 == random_number:
            self.game_balance += 80
            self.balance.setText(f"Balance:{self.game_balance}с")
            self.attemps.setText(f"Win")
            self.start_game()
            self.get_random_number = self.__generate_random_number()
            
    def three_button(self, random_number):
        num3 = int(self.three.text())
        if num3 == random_number:
            self.game_balance += 80
            self.balance.setText(f"Balance:{self.game_balance}с")
            self.attemps.setText(f"Win")
            self.start_game()
            self.get_random_number = self.__generate_random_number()
            
    def four_button(self, random_number):
        num4 = int(self.four.text())
        if num4 == random_number:
            self.game_balance += 80
            self.balance.setText(f"Balance:{self.game_balance}с")
            self.attemps.setText(f"Win")
            self.start_game()
            self.get_random_number = self.__generate_random_number()
            
    def five_button(self, random_number):
        num5 = int(self.five.text())
        if num5 == random_number:
            self.game_balance += 80
            self.balance.setText(f"Balance:{self.game_balance}с")
            self.attemps.setText(f"Win")
            self.start_game()
            self.get_random_number = self.__generate_random_number()
    
    def six_button(self, random_number):
        num6 = int(self.six.text())
        if num6 == random_number:
            self.game_balance += 80
            self.balance.setText(f"Balance:{self.game_balance}с")
            self.attemps.setText(f"Win")
            self.start_game()
            self.get_random_number = self.__generate_random_number()
            
    def seven_button(self, random_number):
        num7 = int(self.seven.text())
        if num7 == random_number:
            self.game_balance += 80
            self.balance.setText(f"Balance:{self.game_balance}с")
            self.attemps.setText(f"Win")
            self.start_game()
            self.get_random_number = self.__generate_random_number()
        
    def eight_button(self, random_number):
        num8 = int(self.eight.text())
        if num8 == random_number:
            self.game_balance += 80
            self.balance.setText(f"Balance:{self.game_balance}с")
            self.attemps.setText(f"Win")
            self.start_game()
            self.get_random_number = self.__generate_random_number() 
            
    def nine_button(self, random_number):
        num9 = int(self.nine.text())
        if num9 == random_number:
            self.game_balance += 80
            self.balance.setText(f"Balance:{self.game_balance}с")
            self.attemps.setText(f"Win")
            self.start_game()
            self.get_random_number = self.__generate_random_number()
            
    def ten_button(self, random_number):
        num10 = int(self.ten.text())
        if num10 == random_number:
            self.game_balance += 80
            self.balance.setText(f"Balance:{self.game_balance}с")
            self.attemps.setText(f"Win")
            self.start_game()
            self.get_random_number = self.__generate_random_number()        
    
         
app = QApplication(sys.argv)
ran = RandomWindow()
ran.show()
app.exec_()