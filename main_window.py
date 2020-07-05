"""This file encloses the code for the main window which is displayed when the program starts, which includes the options for starting game, settings, and more"""
#TODO: Add conditionals to the imports to enable cross-platform compatibility
import tkinter as TK

#Components are stacked together, buttons in a group, labels in another, etc. Naming convention for component Objects: camelCaseNaming


mainContainer=TK.Tk()

testLabel_text=TK.StringVar()

testLabel=TK.Label(mainContainer, textvariable=testLabel_text, relief=TK.RAISED)


def start_intro_window():
	testLabel_text.set("Everything looks good for now")
	testLabel.pack()

	mainContainer.mainloop()

start_intro_window()
