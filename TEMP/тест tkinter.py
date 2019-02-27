
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Животный мир")
root.geometry("1920x1080+0+0")

img = Image.open('top.png')
photo = ImageTk.PhotoImage(img)
image = PhotoImage(name=photo)
button = Button(root,image=image)
root.mainloop()
