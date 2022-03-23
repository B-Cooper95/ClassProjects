"""
Graphical User Interfaces with Tk -Python Documentation
https://docs.python.org/3/library/tk.html

Modern Tkinter:
https://tkdocs.com/tutorial/index.html

• older official documentation
    https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html

tKinter Repository:
https://github.com/roseman/tkdocs

"""

'''
AP Considerations:
    •   Project needs to be ACHIEVABLE:
        •   Build this only within the constraints of what Create PT is
            asking for.
                • Data must be stored in a list
                • You must use a function with one or more parameters 
                  and include sequencing, selection, and iteration.
                    • Sequencing - Application of each step of an algorithm in order.
                    • Selection - Branching Statements: If/Else, Try/Catch
                    • Iteration - Loops.
            
    •   I cannot give you feedback on your project or help you solve problems.
         • Can help solve very similar problems.
	• You and your classmates may work together on a project, but you 
	must have your own separate contributions that act as parts of a whole.

Other things:
    •   Comments comments comments. You will not remember what each of these
        things do, and as we continue to improve on our projects, the progression
        of how we got from A to B to C in our project will disappear.

'''
import tkinter as tk
from PIL import Image, ImageTk

# Initializes window specs
root = tk.Tk()
canvas = tk.Canvas(root, height = 450, width = 300, bg = "#C0C0C0")
canvas.grid(rowspan=3, columnspan=3)

gradesList = []

# Loads an image into python and makes it compatible for tkinter use.
logo = Image.open("CalcLogo.png")
#logo.show()
logo = ImageTk.PhotoImage(logo)
logoLabel = tk.Label(root, image=logo, bg = "#C0C0C0")
logoLabel.grid(row=0, column=1)

# Next time, need to modify the welcome text
# add the logo, and stylize the app a little more.
# • Styles: change start button to orange, lengthen height to 500,
#   change active bg and fg of buttons. Change background color of
#   program to a darker gray.

# Initializes all of the remaining primary objects for the project.
def start():
    global avg_btn, entry

    welcome_txt.config(text="Enter a number.")

    entry = tk.Entry(beFrame, font=("Raleway", 12))
    entry.bind("<Return>", _getEntry)
    entry.grid(row=0, sticky="WE")

    start_btn.config(width=10, command=lambda:getEntry())
    start_btn.grid(sticky="W")


    avg_btn = tk.Button(beFrame, text="Calc.\nAvg.",
                      command=lambda: calcAvg(gradesList), height = 2, width =9,
                      font = ("Raleway",12), bg="#000000", fg="white",
                      activebackground="#808080")

    avg_btn.grid(row=1, sticky="E")

# Allows us to enter ONLY numbers into the entry box.
def getEntry():
    try:
        gradesList.append(int(entry.get()))
        welcome_txt.config(text=stringBuilder(gradesList))

    except:
        welcome_txt.config(text="Enter a valid number.")

    entry.delete(0,len(entry.get()))
    start_txt.set("Get")

# Keyboard event handler for the enter key (attaches to entry box)
def _getEntry(event):
    getEntry()

# Builds/Formats a string out of our grades list.
# Accounts for commas at the end of the string.
def stringBuilder(myList):
    myString = "Grades:\n"
    for i in range(len(myList)):
        if (i == len(myList) - 1):
            myString += str(myList[i])
        else:
            myString += str(myList[i]) + ", "
            if ((i + 1) % 4 == 0 and i != 0):
                myString += "\n"
    return myString

def calcAvg(myList):
    avg = round( sum(myList) / len(myList) ,2 )
    end(avg)

# Establishes the end screen and displays our final average.
def end(num):
    myString = "Average:\n"+str(num)
    welcome_txt.config(text=myString)
    entry.destroy()
    avg_btn.destroy()
    gradesList.clear()

    start_txt.set("Restart")
    start_btn.config(width=15, command=lambda:start())

# We use frame to subdivide a section of the window.
beFrame = tk.Frame(root)
beFrame.grid(row=2, column = 1)

# Creates the main button that will be used throughout the program.
start_txt = tk.StringVar()
start_btn = tk.Button(beFrame, textvariable=start_txt,
                      command=lambda: start(), height = 2, width =15,
                      font = ("Raleway",12), bg="#ff6f00", fg="white",
                      activebackground="#b83d00")
start_txt.set("Start")
start_btn.grid(row=1, sticky="WE")


# Creates our main Label object that we update throughout the program.
welcome_txt = tk.Label(root, text="Welcome!", font=("Raleway", 22), bg = "#C0C0C0")
welcome_txt.grid(column=1, row=1) # Used to manage the placement of objects.

# Keeps things centered.
root.rowconfigure([0,1,2], weight=1)
root.columnconfigure([0,1,2], weight=1)
root.mainloop()