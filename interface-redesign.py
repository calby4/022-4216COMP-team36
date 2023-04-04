import customtkinter as ctk
import tkinter as tk

"""
class applicationWindow         CTk 
func __init__                   initialises the main frame of the application

"""

class applicationWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Movie Database")


        self.searchLabel = ctk.CTkLabel(self, text = "Enter Title")
        self.searchLabel.grid(row = 0, column = 0, padx = 20, pady = 20)

        self.searchTextField = ctk.CTkTextbox(self, width=800, height=80)
        self.searchTextField.grid(row = 1, column = 0, padx = 20, pady = 20)

        self.searchButton = ctk.CTkButton(self, text = "Hello, World!", command=self.searchButton_click)
        self.searchButton.grid(row = 1, column = 1, padx = 20, pady = 20)

        """
        self.checkBox1Value = tk.IntVar(value=0)
        self.checkBox1 = ctk.CTkCheckBox(self, text="Hello, World!", variable = self.checkBox1Value, onvalue=1, offvalue=0, command=self.checkBox1_func)
        self.checkBox1.grid(row = 0, column = 1, padx=20, pady=20)
        """
    def searchButton_click(self):
        print("Button was clicked!")

    def checkBox1_func(self):
        if self.checkBox1Value.get() == 0:
            print("Off")
        else:
            print("On")

if __name__ == "__main__":
    mainApp = applicationWindow()
    mainApp.mainloop()