import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title(" My Python Application")
window.geometry("400x300")
window.iconbitmap(default='images\\myicon.ico')
window.resizable(0, 0)


def show_hello():
    messagebox.showinfo('Hello Medium', ' Hello Medium')


myimage = tkinter.PhotoImage(file="images\\python_to_exe.png")

image = tkinter.Label(window, image=myimage, width=500, height=170, )
image.place(x=20, y=60)
image.pack()

space = tkinter.Label(window, height=2, ).pack()

button = tkinter.Button(text=" Hello ", command=show_hello)
button.pack()

window.mainloop()