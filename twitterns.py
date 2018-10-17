import csv
from tkinter import *

with open("Twitter.csv", "a", newline="") as myCSVFile:
    write = csv.writer(myCSVFile, delimiter=";")



    class App(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.grid()
            self.output()

        def output(self):
            Label(text="Vul hier uw naam in:", background="yellow").grid(row=1, sticky=W)
            self.naam = Entry(root, background="yellow")
            self.naam.grid(row=1, sticky=E)

            Label(text="Vul hier uw recensie in(maximaal 140 karakters):", background="yellow").grid(row=2)
            self.recensie = Entry(root, background="yellow")
            self.recensie.grid(row=3)

            self.button= Button(root, text="Submit", command=self.writetofile)
            self.button.grid(row=4)

        def writetofile(self):
            if len(self.recensie.get()) <= 140:
                write.writerow([self.naam.get(), self.recensie.get()])
                quit()
            else:




    if __name__=="__main__":
        root = Tk()
        root.title("Twitter NS")
        root.geometry("500x150")
        root.configure(background='yellow')
        app=App(master=root)
        app.mainloop()
        root.mainloop()

