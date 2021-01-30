from tkinter import *
import time

class Scene():

    def generateWindow():
        window = Tk()
        window.title('My first GUI')
        window.geometry("600x400+1000+300")

        btn = generateButton(window)
        btnTime = generateButtonTime(window)

        btn.pack()
        btnTime.pack()

        window.mainloop()

    def __init__(self):
        self.

    def generateButtonTime(window):
        return Button(window, text="CheckTime", command=checkTime)

    def action():
        print('НАЖАТО')

    def checkTime():
        print(time.strftime('%H:%M:%S'))

    def generateButton(window):
        return Button(window, text="BOTTON", command=action)


##########################################################
generateWindow()

