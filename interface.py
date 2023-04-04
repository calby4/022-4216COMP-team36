# Interface for data sorting program

# Import required libraries
 
import customtkinter as ctk
import tkinter as tk
 
 # Setting the theme of the UI
ctk.set_appearance_mode("dark")
 
ctk.set_default_color_theme("green")   
 
 # Dimensions of the app are set
appWidth, appHeight = 800, 700
 
# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        # Title of the APP
        self.title("DataSorterz")
        self.geometry(f"{appWidth}x{appHeight}")
 
        # Search Label
        self.searchLabel = ctk.CTkLabel(self,
                                      text="Search")
        self.searchLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Search Entry Field
        self.searchEntry = ctk.CTkEntry(self,
                         placeholder_text="Enter search query")
        self.searchEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
        

 
        # Genre choice label
        self.choiceLabel = ctk.CTkLabel(self,
                                        text="Select Genre")
        self.choiceLabel.grid(row=3, column=0,
                              padx=20, pady=20,
                              sticky="ew")
 
        # Genre check boxes
        self.checkboxVar = tk.StringVar(value="Choice 1")
         
        self.choice1 = ctk.CTkCheckBox(self, text="choice 1",
                                       variable=self.checkboxVar,
                                       onvalue="choice1",
                                       offvalue="c1")
        self.choice1.grid(row=3, column=1, padx=20,
                          pady=20, sticky="ew")
 
        self.choice2 = ctk.CTkCheckBox(self, text="choice 2",
                                       variable=self.checkboxVar,
                                       onvalue="choice2",
                                       offvalue="c2")                              
        self.choice2.grid(row=3, column=2, padx=20, pady=20,
                          sticky="ew")
        
        self.choice3 = ctk.CTkCheckBox(self, text="choice 3",
                                       variable=self.checkboxVar,
                                       onvalue="choice3",
                                       offvalue="c3")                              
        self.choice3.grid(row=3, column=3, padx=20, pady=20,
                          sticky="ew")
        
        self.choice4 = ctk.CTkCheckBox(self, text="choice 4",
                                       variable=self.checkboxVar,
                                       onvalue="choice4",
                                       offvalue="c4")                              
        self.choice4.grid(row=3, column=4, padx=20, pady=20,
                          sticky="ew")
        
        self.choice5 = ctk.CTkCheckBox(self, text="choice 5",
                                       variable=self.checkboxVar,
                                       onvalue="choice5",
                                       offvalue="c5")
        self.choice5.grid(row=4, column=1, padx=20,
                          pady=20, sticky="ew")
 
        self.choice6 = ctk.CTkCheckBox(self, text="choice 6",
                                       variable=self.checkboxVar,
                                       onvalue="choice6",
                                       offvalue="c6")                              
        self.choice6.grid(row=4, column=2, padx=20, pady=20,
                          sticky="ew")
        
        self.choice7 = ctk.CTkCheckBox(self, text="choice 7",
                                       variable=self.checkboxVar,
                                       onvalue="choice7",
                                       offvalue="c7")                              
        self.choice7.grid(row=4, column=3, padx=20, pady=20,
                          sticky="ew")
        
        self.choice8 = ctk.CTkCheckBox(self, text="choice 8",
                                       variable=self.checkboxVar,
                                       onvalue="choice8",
                                       offvalue="c8")                              
        self.choice8.grid(row=4, column=4, padx=20, pady=20,
                          sticky="ew")
        
        # Sort Label
        self.sortLabel = ctk.CTkLabel(self,
                                    text="Sort Order")
        self.sortLabel.grid(row=6, column=0,
                                  padx=20, pady=20,
                                  sticky="ew")
 
        # Sort Option Menu
        self.sortOptionMenu = ctk.CTkOptionMenu(self,
                                       values=["Ascending",
                                       "Descending"])
        self.sortOptionMenu.grid(row=6, column=1,
                                       padx=20, pady=20,
                                       columnspan=2, sticky="ew")
 
 
if __name__ == "__main__":
    app = App()
    app.mainloop()