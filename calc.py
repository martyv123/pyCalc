from Tkinter import *

class CalcGUI:
    """GUI for calculator"""
    def __init__(self, master):
        self.master = master # root
        master.title("Python Calculator") # application name and main window

        # Initial totals

        self.total = 0
        self.entered_number = 0

        # Labels

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total")  # label of text

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        # Buttons and functionality

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.multiply_button = Button(master, text="*", command=lambda: self.update("multiply"))
        self.divide_button = Button(master, text="/", command=lambda: self.update("divide"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        self.num0_button = Button(master, text="0", command=lambda:self.numSelect("0"))
        self.num1_button = Button(master, text="1", command=lambda:self.numSelect("1"))
        self.num2_button = Button(master, text="2", command=lambda:self.numSelect("2"))
        self.num3_button = Button(master, text="3", command=lambda:self.numSelect("3"))
        self.num4_button = Button(master, text="4", command=lambda:self.numSelect("4"))
        self.num5_button = Button(master, text="5", command=lambda:self.numSelect("5"))
        self.num6_button = Button(master, text="6", command=lambda:self.numSelect("6"))
        self.num7_button = Button(master, text="7", command=lambda:self.numSelect("7"))
        self.num8_button = Button(master, text="8", command=lambda:self.numSelect("8"))
        self.num9_button = Button(master, text="9", command=lambda:self.numSelect("9"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=4, columnspan=5, sticky=E)

        self.entry.grid(row=1, column=2, columnspan=5, sticky=E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.multiply_button.grid(row=2, column=2)
        self.divide_button.grid(row=2, column=3)
        self.reset_button.grid(row=2, column=4, sticky=E)

        self.num7_button.grid(row=3, column=0, sticky=W+E)
        self.num8_button.grid(row=3, column=1, sticky=W+E)
        self.num9_button.grid(row=3, column=2, sticky=W+E)

        self.num4_button.grid(row=4, column=0, sticky=W+E)
        self.num5_button.grid(row=4, column=1, sticky=W+E)
        self.num6_button.grid(row=4, column=2, sticky=W+E)

        self.num1_button.grid(row=5, column=0, sticky=W+E)
        self.num2_button.grid(row=5, column=1, sticky=W+E)
        self.num3_button.grid(row=5, column=2, sticky=W+E)

        self.num0_button.grid(row=6, column=1, sticky=W+E)

    def validate(self, new_text):
        """
        Validates user input. Returns true if a valid input and false otherwise.

        @param: new_text - str
        """
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        """
        Calculator functions that update the total.

        @param: method - str
        """
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        elif method == "multiply":
            self.total *= self.entered_number
        elif method == "divide":
            self.total /= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

    def numSelect(self, num):
        """
        Displays the number when it is clicked on the calculator

        @param: num - str
        """
        switch (num) {
            case "0":
            
        }
        if num == "0":
            self.entered_number = num
            self.entry.delete(0, END)
            self.entry.insert(0, num)
  
root = Tk() # creates root window
calcGUI = CalcGUI(root) # GUI implementation takes in Tkinter instance
root.mainloop() # start application

print "The application has closed."