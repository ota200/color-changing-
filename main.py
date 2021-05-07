from tkinter import *

root = Tk()

e = Entry(root)
e.pack()

def color_name():
	root.configure(bg=word)

def hex_code():
	h = "#"+word
	root["background"] = h




def background():
	global word
	word = e.get()
	color_name()
	print(word)

def background_hex():
	global word
	word = e.get()
	hex_code()
	print(word)



def b():
	b = Button(text="change bg with color name",command=background)
	b.pack()

def b_():
	b_ = Button(text="change bg with hex_code",command=background)
	b_.pack()


b_()
b()
	

root.mainloop()