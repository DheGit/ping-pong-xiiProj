"""This file encloses the code for the main window which is displayed when the program starts, which includes the options for starting game, settings, and more"""
#TODO: Add conditionals to the imports to enable cross-platform compatibility
import tkinter as TK
from resources import *

#Components are stacked together, buttons in a group, labels in another, etc. Naming convention for component Objects: camelCaseNaming

mainContainer=TK.Tk()

testLabel_text=TK.StringVar()
testLabel=TK.Label(mainContainer, textvariable=testLabel_text, relief=TK.SUNKEN)

p1EntryLabel=TK.Label(mainContainer, text=r_p1_name_label_txt)
p2EntryLabel=TK.Label(mainContainer, text=r_p2_name_label_txt)

p1NameEntry=TK.Entry(mainContainer)
p2NameEntry=TK.Entry(mainContainer)

quitButton=TK.Button(mainContainer, text=r_quit_button_txt, command=mainContainer.quit)

"""init_layout(): Contains the initialisation code for the layout, including the styling"""
def init_layout():
	global testLabel_text, testLabel, mainContainer
	mainContainer.minsize(window_height, window_width)
	
	testLabel_text.set(r_test_label_txt)
	testLabel.pack(side=TK.TOP, padx=10, pady=10)

	global p1NameEntry, p2NameEntry, p1EntryLabel, p2EntryLabel
	p1EntryLabel.pack()
	p2EntryLabel.pack()
	p1NameEntry.pack()
	p2NameEntry.pack()

	global quitButton
	quitButton.pack(side=TK.TOP)


def start_intro_window():
	init_layout()
	mainContainer.mainloop()

start_intro_window()
