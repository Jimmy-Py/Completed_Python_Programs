# Jimmy, "Order Up" demonstration of Dawson Chapter10 Tkinter concepts.

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        """ Initialize frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "Please select a drink:").grid(row = 0, column = 0)

        # create water check buttons
        self.water = BooleanVar()
        Checkbutton(self,
                    text = "Water, $1",
                    variable = self.water,
                    ).grid(row = 0, column = 1)

        # create orange juice check button.
        self.orange_juice = BooleanVar()
        #self.orange_juice = False
        Checkbutton(self,
                    text = "Freshly Squeezed Orange Juice, $2",
                    variable = self.orange_juice
                    ).grid(row = 0, column = 2)

        # create button to display bill.
        Button(self,
               text = "Click to display bill.",
               command = self.display_bill
               ).grid(row = 1, column = 0, columnspan = 3)

        # create box to display bill in.
        self.bill_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.bill_txt.grid(row = 100, column = 0, columnspan = 4)


    def display_bill(self):
        self.calculate_bill()
        self.bill_txt.delete(0.0, END)
        self.bill_txt.insert(0.0, self.total)

    def calculate_bill(self):
        self.total = 0
        if self.water.get():
            self.total += 1
        if self.orange_juice.get():
            self.total += 2

root = Tk()
root.title("Jimmy's Diner")
app = Application(root)
root.geometry("3000x3000")
root.mainloop()






