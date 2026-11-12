from tkinter import *
root = Tk()
root.title("Main Window 1")
root.geometry("500x500")
label1= Label(root, text="This is the main window" )
def command1():
    new_window=Toplevel(root)
    new_window.title("New Window 1")
    new_window.geometry("500x500")
    label2= Label(new_window, text="This is the new window")
    label2.pack()
    new_window.mainloop()
button1= Button(root, text="Click Me", command=command1)
label1.pack()
button1.pack()



































root.mainloop()