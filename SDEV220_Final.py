from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()

canvas = Canvas(root, width = 200, height = 300)
canvas.grid(columnspan = 3, rowspan=3)

root.title("Applebees Recipe Book")
root.geometry("400x400")

#Backgound Image
Background_Image = PhotoImage(file="C:/Users/cguil/OneDrive/Pictures/Screenshots/Applebees_Background.png")



my_Label= Label(root, image = Background_Image)
my_Label.place(x=0, y=0, relwidth=1, relheight=1)

#Searchbar
search_entry = Entry(root, width = 30)
search_entry.grid(row = 1, column = 1)

def get_recipe(catagory):
    conn = sqlite3.connect('recipes.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM recipes WHERE catagory =?", (catagory,))
    recipes = curs.fetchall()
    conn.close()
    return recipes

#Recipe functions
def show_Recipe():
    top = Toplevel()
    catagory = clicked.get()
    recipe = get_recipe(catagory)
    top.title(catagory)
    top.geometry("400x400")

        
#Recipe Buttons
clicked = StringVar()
clicked.set("Recipes")
drop_down = OptionMenu(root,clicked, "Appitizer", "Entree", "Dessert")
drop_down.grid(row = 2, column = 0)

show_button= Button(root, text = "Show Recipes",padx = 30,command = show_Recipe)
show_button.grid(row = 3, column = 1)

#Drink Button
Drink_Button = Button(root, text = "Drink Recipes",padx = 30)
Drink_Button.grid(row = 2, column = 3)


root.mainloop() 