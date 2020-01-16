from Tkinter import Tk, Label, Button

class CalcGUI:
    """GUI for calculator"""
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator") # application name

        self.label = Label(master, text="Python Calculator.")  # GUI title
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command = self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command = master.quit)
        self.close_button.pack()

    def greet(self):
        """Greets the user"""
        print "Greetings!"
    
root = Tk()
calcGUI = CalcGUI(root)
root.mainloop()