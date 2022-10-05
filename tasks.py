# # 1. Создать класс TrafficLight (светофор):
# # ● определить у него один атрибут color (цвет) и метод running (запуск);
# # ● атрибут реализовать как приватный;
# # ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# # зелёный;
# # ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# # (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# # ● переключение между режимами должно осуществляться только в указанном порядке
# # (красный, жёлтый, зелёный);
# # ● проверить работу примера, создав экземпляр и вызвав описанный метод.

# from time import sleep
# from termcolor import colored, cprint
# import tkinter as tk


# class TrafficLight(tk.Tk):
#     __dictColor = {"red": 7, "yellow": 2, "green": 10}
#     __color = "red"
#     counter = __dictColor["red"]

#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.lightLabel = tk.Label(self, text="7", width=6, height=3,
#                                    font="times 80", background=self.__color)
#         self.lightLabel.pack(anchor=tk.CENTER, expand=1)

#     def running(self):
#         if self.counter >= 0:
#             if self.__color == "red":
#                 self.lightLabel.configure(text=f"{self.counter}")
#                 self.counter -= 1
#                 self.after(1000, self.running)
#                 if self.counter == -1:
#                     self.__color = "yellow"
#                     self.lightLabel.configure(background=self.__color)
#                     self.counter = self.__dictColor["yellow"]
#             elif self.__color == "yellow":
#                 self.lightLabel.configure(text=f"{self.counter}")
#                 self.counter -= 1
#                 self.after(1000, self.running)
#                 if self.counter == -1:
#                     self.__color = "green"
#                     self.lightLabel.configure(background=self.__color)
#                     self.counter = self.__dictColor["green"]
#             elif self.__color == "green":
#                 self.lightLabel.configure(text=f"{self.counter}")
#                 self.counter -= 1
#                 self.after(1000, self.running)
#                 if self.counter == -1:
#                     self.__color = "red"
#                     self.lightLabel.configure(background=self.__color)
#                     self.counter = self.__dictColor["red"]


# traf = TrafficLight()
# traf.running()
# traf.mainloop()


##########################################################################

# 2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


from operator import length_hint


class Road():

    thick = 5
    massOneMeter = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculateMass(self):
        return str(self._width * self._length * self.massOneMeter * self.thick/1000) + " tonns"


roadA = Road(5000, 20)
print(roadA.calculateMass())
roadB = Road(1000, 10)
roadB.thick = 10
roadB.massOneMeter = 30
print(roadB.calculateMass())
