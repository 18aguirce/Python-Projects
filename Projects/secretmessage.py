# Author: Cesar Vicente
# Date  : April 24, 2019
# This program is derived from the original shell appliction
# called stringmanip.py This program uses the Tkinter GUI.

#from tkinter import*
import tkinter

def scram():
    myString = entInput.get()
    scrambletable = ''.maketrans('abcdefghijklmnopqrstuvwxyz',
                             'zyxwvutsrpqonmlkjihgfedcba')

    scramble = myString.translate(scrambletable)
    # print(scramble) # We took this out
    entOutput.delete(0, tkinter.END)
    entOutput.insert(0, scramble)
    

# Program execution starts here...
# Create and build our screen.

root = tkinter.Tk();
root.title("Scramble / Descramble")
root.geometry("235x200")

lblDirections = tkinter.Label(root, text="Enter some text to be scrabled.")
entInput = tkinter.Entry(root)
btnScramble = tkinter.Button(root, text="Scramble",
                             fg="#0000FF", bg="#CCCCCC",
                             command=scram)
entOutput = tkinter.Entry(root)
lblCredits = tkinter.Label(root, text="\u00A9 John Doe")

lblDirections.grid(padx=5, pady=5)
entInput.grid(padx=5, pady=5)
btnScramble.grid(padx=5, pady=5)
entOutput.grid(padx=5, pady=5)
lblCredits.grid(padx=5, pady=5)

root.mainloop()

#GUI - Graphical User Interface
