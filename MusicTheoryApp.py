import tkinter as tk
from PIL import ImageTk, Image


def scaleGen(key, Mm):
    try:
        alphabet = ["A", "A#", "B", "C", "C#", "D", "D#", "E","F", "F#", "G", "G#"]
        idx = alphabet.index(key)
        if Mm == "major":
            pattern = [0, 2, 4, 5, 7, 9, 11, 12]
        if Mm == "minor":
            pattern = [0, 2, 3, 5, 7, 8, 10, 12]
        scale = ""
        for val in pattern:
            scale+= alphabet[(idx + val)%12]+" "
        scaleName = key+" "+Mm+":\n"

        finalOutput = scaleName+scale

        return finalOutput

    except (ValueError, UnboundLocalError):
        invalidshow()

root= tk.Tk()
root.config(bg="#800800")
canvas= tk.Canvas(width=325, height=400, bg="#800800")


canvas.grid(rowspan=3, columnspan=3)


def show():
    txt["state"] = "normal"
    txt.delete('1.0', tk.END)
    scale = "\n\n"+scaleGen(clicked1.get(), clicked2.get())
    txt.insert(tk.END, scale)
    txt.tag_add("center", "1.0", "end")
    txt["state"] = "disabled"

def invalidshow():
    txt["state"] = "normal"
    txt.delete('1.0', tk.END)
    txt.insert(tk.END, "Please select a Key and a Scale")
    txt.tag_add("center", "1.0", "end")
    txt["state"] = "disabled"

frame = tk.Frame(root)
frame.grid(row=1, column=1)

alphabet = ["A", "A#", "B", "C", "C#", "D", "D#", "E","F", "F#", "G", "G#"]
scale = ["major", "minor"]

clicked1 = tk.StringVar()
clicked1.set("Key")



drop = tk.OptionMenu(frame, clicked1, *alphabet )
drop.grid(row=1,column=1)
drop.config(bg="#C00800", activebackground="#DD0800",
            fg="White", activeforeground="#808080",
            font="Raleway 12", height=2, width=7)

drop["menu"].config(bg="#C00800", activebackground="#DD0800",
                    fg="White", activeforeground="#808080",
                    font="Raleway 12")



clicked2 = tk.StringVar()
clicked2.set("Scale")

drop2 = tk.OptionMenu(frame, clicked2, *scale)
drop2.grid(row=1,column=2)

drop2.config(bg="#C00800", activebackground="#DD0800",
            fg="White", activeforeground="#808080",
            font="Raleway 12", height=2, width=7)

drop2["menu"].config(bg="#C00800", activebackground="#DD0800",
                     fg="White", activeforeground="#808080",
                     font="Raleway 12")

selButton = tk.Button(root, text="Show", height=3, width=20, borderwidth=3, relief="raised",
                            bg="#C00800", activebackground="#DD0800",
                            fg="White", activeforeground="#808080",
                            font="Raleway 15",  command=lambda:show()).grid(row=2, column=1)


txt = tk.Text(root, relief = "sunken", bg="#ff8888",width = 20, height=6, font="Raleway 17", borderwidth=4, state="disabled")
txt.tag_config("center", justify="center")
txt.grid(row=0, column=1)

root.rowconfigure([0,1,2], weight=1)
root.columnconfigure([0,1,2], weight=1)

root.mainloop()