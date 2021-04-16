import json 
from datetime import *

weeked = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]

def woring():
    NAME = input("введите название вещи что выходит\n")
    DAY = input("назовите день недели выхода(с большой буквы)\n")
    information[NAME] = DAY

class data_qith():
    
    def __init__(self,name,day_of_the_week):
        self.name = name
        self.data_one = weeked.index(day_of_the_week) + 1
    
    
    def info(self):
        data = datetime.today()
        weeked_one = datetime.isoweekday(data)
        if self.data_one < weeked_one :
            data_two = 7 - weeked_one + self.data_one
            if data_two == 1:
                print("До", self.name ,"остался",str(data_two), "день")
            elif data_two > 1:
                print("До", self.name ,"осталось",str(data_two), "дней")
        elif self.data_one > weeked_one:
            data_two = self.data_one - weeked_one
            if data_two == 1:
                print("До", self.name ,"остался",str(data_two), "день")
            elif data_two > 1:
                print("До", self.name ,"осталось",str(data_two), "дней")
        else:
            print(self.name ,"вышел или выйдет сегодня")
            

with open("information.json","r",encoding="UTF-8") as file:
    information = json.load(file)

going = input("хотите добавить дату да\нет\n")
while going != "нет":
    woring()
    going = input("котите добавить дату да\нет\n")

for i in information:   
    work = data_qith(i,information[i])
    work.info()

with open("information.json","w",encoding="UTF-8") as file:
    json.dump(information,file)












