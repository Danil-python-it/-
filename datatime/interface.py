#region библиотеки
import json 
from datetime import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QWidget,QRadioButton,QMessageBox,QLineEdit,QInputDialog,QLabel,QPushButton,QHBoxLayout
#endregion

#region основные ностройки
data = datetime.today()
weeked_one = datetime.isoweekday(data)
weeked = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
array = list()
names_and_text = dict()
informa = dict()
#endregion
  
#region создание необходимых функций
def function_button():
    name, result = QInputDialog.getText(string, "добавляем дату", "название даты")
    data, result = QInputDialog.getText(string, "добавляем дату", "название дня недели выхода(С большой буквы)")
    with open("information.json" , "r" , encoding="UTF-8") as file:
        inform = json.load(file)
    inform[name] = data
    informa[name] = data
    for i in informa:
        kam = data_boss(i,informa[i])
        kam.button()
        array.append(kam)
    del informa[name]
    with open("information.json", "w" , encoding="UTF-8") as file:
        json.dump(inform,file)

def function_button_two():
    name2, result = QInputDialog.getText(string, "удаляем дату", "название даты")
    with open("information.json","r" , encoding="UTF-8") as file:
        informati_two = json.load(file)
    del informati_two[name2]
    with open("information.json", "w" , encoding="UTF-8") as file:
        json.dump(informati_two, file)
#endregion

#region классы
class data_boss():

    def __init__(self,name,day,text=None):
        self.name = name 
        self.data_one = weeked.index(day)+1
        if self.data_one < weeked_one :
            data_two = 7 - weeked_one + self.data_one
            if data_two == 1:
                self.text = "До " + self.name + " остался "+ str(data_two) + " день"
            elif data_two == 6 or data_two == 5 or data_two == 7:
                self.text = "До " + self.name + " осталось " + str(data_two) + " дней"            
            elif data_two > 1 :
                self.text = "До " + self.name + " осталось " + str(data_two) + " дня"
        elif self.data_one > weeked_one:
            data_two = self.data_one - weeked_one
            if data_two == 1:
                self.text = "До " + self.name + " остался " + str(data_two) + " день"
            elif data_two == 6 or data_two == 5 or data_two == 7:
                self.text = "До " + self.name + " осталось " + str(data_two) + " дней"            
            elif data_two > 1:
                self.text = "До " + self.name + " осталось " + str(data_two) + " дня"
        else:
            self.text = self.name + " вышел или выйдет сегодня"
        
        names_and_text[self.name] = self.text
    
    def button(self):
        def function():
            message = QMessageBox()
            message.setText(names_and_text[self.name])    
            message.exec_()
        btn = QRadioButton(self.name)
        btn.clicked.connect(function)
        if len(array) <= 7:   
            layout_two.addWidget(btn,alignment=Qt.AlignCenter)
        else:
            layout_one.addWidget(btn,alignment=Qt.AlignCenter)
#endregion

#region вызов текстовых документов
with open("information.json" , "r" , encoding="UTF-8") as file:
    inform = json.load(file)
#endregion 

#region настройка интерфейса 
app = QApplication([])
main = QWidget()
main.setWindowTitle('BETA:TEST:БЛОКНОТ')
string = QLineEdit()
button_two = QPushButton("добавить новую дату")
button_three = QPushButton("удалить дату")
button_two.clicked.connect(function_button)
button_three.clicked.connect(function_button_two)
layout_two = QVBoxLayout()
layout_one = QVBoxLayout()
layout_three = QVBoxLayout()
layout_fhour = QHBoxLayout()
main.resize(500,500)

for i in inform:
    mak = data_boss(i,inform[i])
    mak.button()
    array.append(mak)

layout_three.addWidget(button_two,alignment=Qt.AlignCenter)
layout_three.addWidget(button_three,alignment=Qt.AlignCenter)

layout_fhour.addLayout(layout_two)
layout_fhour.addLayout(layout_one)
layout_fhour.addLayout(layout_three)

main.setLayout(layout_fhour)
main.show()
app.exec_()
#endregion
