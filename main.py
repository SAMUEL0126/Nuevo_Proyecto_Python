
from Tkinter import *

import sqlite3

class Product:
    def __init__(self,window):
        self.wind = window
        self.wind.title('Products Application')
        
if __name__ == '__main__':
    window = Tk()
    aplication =  Product(window)
    window.mainloop()