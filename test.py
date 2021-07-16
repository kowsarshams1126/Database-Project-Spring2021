from tkinter import *

root = Tk()
root.geometry("150x200")

w = Label(root, text ='GeeksForGeeks',
		font = "50")

w.pack()

scroll_bar = Scrollbar(root)

scroll_bar.pack( side = RIGHT,
				fill = Y )

mylist = Frame(root,
				yscrollcommand = scroll_bar.set )

for line in range(1, 26):
	Label(frame, text=line).pack()

mylist.pack( side = LEFT, fill = BOTH )

scroll_bar.config( command = mylist.yview )

root.mainloop()
